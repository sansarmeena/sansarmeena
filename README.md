# Sansar Raj Meena — personal website

Academic website built on the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme,
laid out like [aguyfromshivalik.github.io](https://github.com/aguyfromshivalik/aguyfromshivalik.github.io):
Home, Research, Publications, News, Contact and Memories.

## Where things live

| What | File |
| --- | --- |
| Name, site URL, author-name highlighting | `_config.yml` (`first_name`, `url`, `scholar:`) |
| Home page text, subtitle, photo | `_pages/about.md`, photo at `assets/img/prof_pic.jpg` |
| Research page | `_pages/research.md` |
| Contact page and map | `_pages/contact.md` |
| News items | `_news/announcement_*.md` (one file per item) |
| Social icons (email, ORCID, Scholar, …) | `_data/socials.yml` |
| Publications | `_bibliography/papers.bib` |
| Memories (photo gallery) | `_data/memories.yml`, photos in `assets/memories/` |

## Updating publications

`papers.bib` is generated from the public ORCID record:

```
python bin/orcid_to_bib.py
```

It keeps journal articles, conference papers and preprints with a DOI, drops EGU abstracts and
discussion preprints that have a final version, and adds `abbr`, `bibtex_show` and `selected`.
Edit `SELECTED`, `SKIP_DOIS` and `MANUAL` at the top of the script to change what is shown.

## Memories

`_pages/memories.md` renders `_data/memories.yml`, newest first, grouped by year. Each event has
`title`, `place`, `date`, `caption`, `category` (conference, visit, fieldwork or award), the
LinkedIn post link(s), and a list of photos. For each photo put `<file>.jpg` (max 1600 px) and
`<file>-thumb.jpg` (480x360 crop) in `assets/memories/`, and give its width and height in the YAML
so the lightbox opens at the right size. Delete an entry (and its files) to remove an event.

## Deploying on GitHub Pages at sansarmeena.com

1. Create a public, empty repository `sansarmeena.github.io` and push this folder to `main`.
2. Repository → Settings → Actions → General → Workflow permissions: **Read and write**.
3. The `Deploy site` workflow builds into the `gh-pages` branch (the `CNAME` file goes with it).
   Settings → Pages → Source: **Deploy from a branch**, branch **gh-pages**, folder `/ (root)`.
4. Namecheap → Domain List → sansarmeena.com → Advanced DNS: delete the parking records
   (the `CNAME www → parkingpage.namecheap.com` and the `URL Redirect @`), then add
   - `A @ 185.199.108.153`, `A @ 185.199.109.153`, `A @ 185.199.110.153`, `A @ 185.199.111.153`
   - `CNAME www sansarmeena.github.io.`
5. Settings → Pages → Custom domain: `sansarmeena.com`, Save, wait for the DNS check, then tick
   **Enforce HTTPS** (the certificate can take up to an hour).
6. Recommended: GitHub → your profile Settings → Pages → **Add a verified domain**, so no one
   else can attach sansarmeena.com to their repository.

## Local preview

Ruby is not needed on Windows; WSL works:

```
cd ~/site && bundle install && bundle exec jekyll serve
```

then open http://localhost:4000.
