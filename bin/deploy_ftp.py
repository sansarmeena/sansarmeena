"""Upload the built website to the sansarmeena.com hosting over FTPS.

Usage:  python bin/deploy_ftp.py [path-to-built-site]

Defaults to C:/Users/sansa/calude_workspace/sansarmeena_site_build (the unzipped
production build). Host, username and remote folder come from bin/ftp_settings.ini;
the password is asked for every time and never stored. Only new or changed files
(by size) are uploaded; nothing on the server is deleted.
"""

import configparser
import ftplib
import getpass
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SETTINGS = HERE / "ftp_settings.ini"
DEFAULT_SITE = Path("C:/Users/sansa/calude_workspace/sansarmeena_site_build")


def load_settings():
    cfg = configparser.ConfigParser()
    if not SETTINGS.exists():
        cfg["ftp"] = {"host": "ftp.sansarmeena.com", "user": "", "remote_dir": "/public_html"}
        cfg.write(open(SETTINGS, "w"))
        sys.exit(f"Created {SETTINGS}. Fill in host, user and remote_dir, then run again.")
    s = cfg["ftp"]
    if not s.get("user"):
        sys.exit(f"Fill in 'user' in {SETTINGS} first.")
    return s["host"], s["user"], s.get("remote_dir", "/public_html")


def remote_sizes(ftp, path):
    """Map of file name -> size for one remote folder (empty if it doesn't exist)."""
    try:
        return {name: int(facts.get("size", -1)) for name, facts in ftp.mlsd(path, ["type", "size"])
                if facts.get("type") == "file"}
    except ftplib.error_perm:
        return {}


def ensure_dir(ftp, path):
    try:
        ftp.mkd(path)
    except ftplib.error_perm:
        pass  # already exists


def main():
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SITE
    if not (site / "index.html").exists():
        sys.exit(f"No index.html in {site}; point me at the unzipped site folder.")
    host, user, remote_root = load_settings()
    password = getpass.getpass(f"FTP password for {user}@{host}: ")

    try:
        ftp = ftplib.FTP_TLS(host, timeout=60)
        ftp.login(user, password)
        ftp.prot_p()
    except ftplib.all_errors as e:
        sys.exit(f"Could not log in over FTPS: {e}")

    uploaded = skipped = 0
    for folder, _, files in os.walk(site):
        rel = Path(folder).relative_to(site).as_posix()
        rdir = remote_root.rstrip("/") + ("" if rel == "." else "/" + rel)
        ensure_dir(ftp, rdir)
        have = remote_sizes(ftp, rdir)
        for name in files:
            local = Path(folder) / name
            if have.get(name) == local.stat().st_size:
                skipped += 1
                continue
            with open(local, "rb") as f:
                ftp.storbinary(f"STOR {rdir}/{name}", f)
            uploaded += 1
            print(f"  up  {rdir}/{name}")
    ftp.quit()
    print(f"\nDone: {uploaded} uploaded, {skipped} unchanged. Check https://sansarmeena.com")


if __name__ == "__main__":
    main()
