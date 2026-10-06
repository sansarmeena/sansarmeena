"""Regenerate _bibliography/papers.bib from the public ORCID record.

Usage:  python bin/orcid_to_bib.py

Pulls every work on ORCID 0000-0001-6175-6491, keeps journal articles,
conference papers and non-abstract preprints that carry a DOI, fetches
Crossref BibTeX for each, and adds the al-folio fields (abbr, selected,
bibtex_show). Entries in MANUAL are appended as-is. Edit SELECTED / SKIP
below, re-run, commit.
"""

import html
import json
import re
import time
import urllib.request
from pathlib import Path

ORCID = "0000-0001-6175-6491"
OUT = Path(__file__).resolve().parent.parent / "_bibliography" / "papers.bib"

KEEP_TYPES = {"journal-article", "conference-paper", "preprint"}
# EGU General Assembly abstracts are preprint-typed on ORCID; leave them out.
SKIP_DOI_PREFIXES = ("10.5194/egusphere-egu",)
# NHESS discussion version of nhess-22-1395-2022, retitled on acceptance.
SKIP_DOIS = {"10.5194/nhess-2021-299"}

# Shown on the home page and starred on /publications/.
SELECTED = {
    "10.5194/essd-15-3283-2023",
    "10.1007/s10346-022-01861-3",
    "10.5194/nhess-22-1395-2022",
    "10.1007/s10346-020-01602-4",
    "10.5194/nhess-21-301-2021",
    "10.31223/x56n4b",
    "10.5194/egusphere-2026-5462",
}

# Thumbnails shown next to an entry, from assets/img/publication_preview/.
PREVIEW = {
    "10.31223/x56n4b": "chronosat.jpg",
    "10.5194/egusphere-2026-5462": "nisar.jpg",
    "10.21203/rs.3.rs-11022365/v1": "nisar.jpg",
}

ABBR = {
    "Remote Sensing": "Remote Sens.",
    "Landslides": "Landslides",
    "Scientific Reports": "Sci. Rep.",
    "Natural Hazards and Earth System Sciences": "NHESS",
    "Earth System Science Data": "ESSD",
    "Engineering Geology": "Eng. Geol.",
    "Geoscience Frontiers": "Geosci. Front.",
    "Gondwana Research": "Gondwana Res.",
    "Natural Hazards": "Nat. Hazards",
    "Geosciences": "Geosciences",
    "Advances in Space Research": "Adv. Space Res.",
    "Transactions in GIS": "Trans. GIS",
    "Frontiers in Earth Science": "Front. Earth Sci.",
    "Environmental Earth Sciences": "Environ. Earth Sci.",
    "Remote Sensing Letters": "RSL",
    "International Journal of Remote Sensing": "IJRS",
    "GIScience & Remote Sensing": "GISci. RS",
    "Geomatics, Natural Hazards and Risk": "GNHR",
    "Journal of Hydrology: Regional Studies": "J. Hydrol. Reg.",
    "Bulletin of Engineering Geology and the Environment": "BEGE",
    "Environmental Science and Pollution Research": "ESPR",
    "ISPRS International Journal of Geo-Information": "IJGI",
    "IEEE Geoscience and Remote Sensing Letters": "IEEE GRSL",
    "IEEE Transactions on Geoscience and Remote Sensing": "IEEE TGRS",
    "Journal of Rock Mechanics and Geotechnical Engineering": "JRMGE",
    "CCF Transactions on High Performance Computing": "CCF THPC",
    "Journal of Geophysical Research: Machine Learning and Computation": "JGR: MLC",
}

MANUAL = r"""
@misc{meena2026chronosatweights,
  title     = {ChronoSat MAE and JEPA Spatial Encoder Weights for Frozen-Probe Very-High-Resolution Landslide Segmentation},
  author    = {Meena, Sansar Raj and Tang, Xiaochuan and Catani, Filippo},
  year      = {2026},
  month     = aug,
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22046362},
  abbr      = {Weights},
  preview   = {chronosat.jpg},
  note      = {Open model weights, two 867M-parameter encoders, CC BY 4.0},
  bibtex_show = {true},
}
@phdthesis{meena2021thesis,
  title     = {Rapid generation of event-based landslide inventory and susceptibility maps using deep learning and Earth observation data},
  author    = {Meena, Sansar Raj},
  school    = {Paris Lodron University of Salzburg, Department of Geoinformatics -- Z\_GIS},
  year      = {2021},
  abbr      = {PhD thesis},
  bibtex_show = {true},
}
"""


def get(url, accept="application/json"):
    for attempt in range(6):
        try:
            req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "orcid_to_bib"})
            return urllib.request.urlopen(req, timeout=40).read().decode("utf8")
        except Exception:
            if attempt == 5:
                raise
            time.sleep(3 * (attempt + 1))


def abbr_for(journal, typ):
    if not journal:
        return "Preprint" if typ == "preprint" else None
    journal = html.unescape(journal)
    if journal in ABBR:
        return ABBR[journal]
    if journal.startswith("IEEE Journal of Selected Topics"):
        return "IEEE JSTARS"
    return None


def main():
    record = json.loads(get(f"https://pub.orcid.org/v3.0/{ORCID}/works"))
    works = []
    for group in record["group"]:
        summary = group["work-summary"][0]
        dois = [e["external-id-value"].lower() for e in group["external-ids"]["external-id"]
                if e["external-id-type"] == "doi"]
        if not dois or summary["type"] not in KEEP_TYPES:
            continue
        doi = dois[0]
        if doi in SKIP_DOIS or doi.startswith(SKIP_DOI_PREFIXES):
            continue
        works.append((doi, summary["type"], summary["title"]["title"]["value"]))

    # Drop preprints (e.g. ESSD/NHESS discussion papers) whose final version is also listed.
    norm = lambda t: re.sub(r"\W", "", t.lower())[:40]
    published = {norm(t) for _, typ, t in works if typ != "preprint"}
    works = [(d, typ) for d, typ, t in works if typ != "preprint" or norm(t) not in published]

    entries, keys = [], set()
    for doi, typ in sorted(set(works)):
        bib = get(f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex",
                  "application/x-bibtex").strip()
        bib = html.unescape(bib).replace("‐", "-").replace("‑", "-")
        bib = re.sub(r"title=\{Article ", "title={", bib)
        # Crossref has the name order swapped on at least one record (10.1007/s11356-020-11004-7).
        bib = bib.replace("Raj, Meena Sansar", "Meena, Sansar Raj")
        bib = re.sub(r",\s*url=\{http://dx\.doi\.org/[^}]*\}", "", bib)
        m = re.match(r"@(\w+)\{([^,]+),", bib)
        year = re.search(r"year=\{(\d{4})\}", bib)
        first = re.search(r"author=\{([^,}]+)", bib)
        word = re.search(r"title=\{\W*(\w+)", bib)
        key = re.sub(r"\W", "", f"{first.group(1) if first else 'anon'}{year.group(1) if year else ''}"
                                f"{word.group(1) if word else ''}").lower()
        while key in keys:
            key += "b"
        keys.add(key)
        journal = re.search(r"journal=\{([^}]*)\}", bib)
        extra = ["bibtex_show={true}"]
        a = abbr_for(journal.group(1) if journal else None, typ)
        if a:
            extra.append(f"abbr={{{a}}}")
        if doi in SELECTED:
            extra.append("selected={true}")
        if doi in PREVIEW:
            extra.append(f"preview={{{PREVIEW[doi]}}}")
        bib = f"@{m.group(1)}{{{key}, " + ", ".join(extra) + ", " + bib[m.end():].lstrip()
        entries.append(bib)
        time.sleep(0.5)

    OUT.write_text("---\n---\n\n" + "\n\n".join(entries) + "\n" + MANUAL, encoding="utf8")
    print(f"wrote {len(entries)} DOI entries + manual entries to {OUT}")


if __name__ == "__main__":
    main()
