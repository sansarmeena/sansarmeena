---
layout: about
title: Home
permalink: /
subtitle: AI and Earth observation for geohazards · Researcher at <a href='https://www.ogs.it/en'>OGS</a>, Trieste · Geophysics Department, SpatioAI Lab
profile:
  align: right
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>Borgo Grotta Gigante 42/C</p>
    <p>34010 Sgonico (TS), Italy</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page (true/false)

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 3 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: false # adds a vertical scroll bar if there are more than 3 new posts items (true/false)
  limit: # leave blank to include all the blog posts (write a number for limit=number)
---

Ciao! 👋

I am a geoinformatics researcher from India working on **artificial intelligence for geohazards**. I build deep-learning models that map landslides and their impacts from satellite and aerial imagery, train Earth-observation **foundation models** on large unlabelled image archives, and use satellite radar, including the new NASA–ISRO **NISAR** mission, to measure how slopes move before and after they fail.

At <a href='https://www.ogs.it/en'>OGS</a> in Trieste I am the Principal Investigator of <a href='https://www.ogs.it/en/projects/natura'><b>NATURA</b></a>, a five-year Starting Grant of the Italian Science Fund (FIS 3, 2026–2031) that combines AI, physically based modelling and socio-economic analysis to understand the natural and anthropogenic drivers of landslide risk in mountain regions.

Before OGS I was a researcher at the Department of Geosciences, <a href='https://www.unipd.it/en/'>University of Padova</a>, in the Machine Intelligence and Slope Stability Laboratory, and at ITC, University of Twente, and a visiting scientist at Boston University. I obtained my PhD in Applied Geoinformatics from the <a href='https://www.plus.ac.at/geoinformatics/'>University of Salzburg</a> (Z_GIS), on deep learning for rapid landslide mapping, and my MSc in Geo-Information Science and Earth Observation from ITC, University of Twente.

<a href='/research/'>Click here</a> to know more about my work. To get in touch, send an email to `smeena[at]ogs[dot]it`.

<style>
  .featured { margin: 2rem 0 1rem; }
  .feat-card { border: 1px solid var(--global-divider-color); border-radius: 8px; overflow: hidden; margin-bottom: 1.25rem; }
  .feat-card img { width: 100%; display: block; border-bottom: 1px solid var(--global-divider-color); background: #fff; }
  .feat-body { padding: .9rem 1.1rem 1rem; }
  .feat-kicker { font-size: .75rem; text-transform: uppercase; letter-spacing: .06em; color: var(--global-theme-color); font-weight: 600; }
  .feat-body h3 { font-size: 1.15rem; margin: .2rem 0 .5rem; }
  .feat-body p { margin-bottom: .6rem; text-align: justify; }
  .feat-links a { display: inline-block; font-size: .85rem; border: 1px solid var(--global-theme-color); border-radius: 4px; padding: .1rem .6rem; margin: 0 .35rem .35rem 0; }
  .feat-note { font-size: .8rem; color: var(--global-text-color-light); }
</style>

<div class="featured">
<h2>featured research</h2>

<div class="feat-card">
  <img src="{{ '/assets/img/featured/chronosat_mae_jepa.jpg' | relative_url }}" alt="Landslide segmentation on 0.2 m aerial images: image, ground truth, MAE prediction and JEPA prediction" loading="lazy">
  <div class="feat-body">
    <div class="feat-kicker">Foundation models · Earth observation · 2026</div>
    <h3>Which self-supervised objective learns landslides? MAE vs JEPA</h3>
    <p>
      With Xiaochuan Tang and Filippo Catani, I trained two vision-transformer foundation models from
      scratch, a masked autoencoder (MAE) and a joint-embedding predictive variant (JEPA), on
      <b>4.85 million unlabelled 0.2 m aerial patches</b> of Emilia-Romagna spanning 1976–2023, and
      compared them for landslide segmentation with frozen encoders from 1 % to 100 % of the labels.
      Under that frozen-probe protocol <b>MAE outperformed JEPA at every label fraction</b>, a hint that
      masked reconstruction keeps the fine morphology of scarps and deposits that landslide mapping needs.
      A fully fine-tuned supervised SegFormer-B2 is still stronger, and the paper says so.
      Both 867-million-parameter encoders are released as open weights, the losing JEPA model included,
      so the comparison can be checked.
    </p>
    <div class="feat-links">
      <a href="https://doi.org/10.31223/X56N4B">Preprint (EarthArXiv)</a>
      <a href="https://doi.org/10.5281/zenodo.22046362">Open weights (Zenodo)</a>
    </div>
    <div class="feat-note">Preprint, not yet peer reviewed; a revised version is in preparation. CC BY 4.0.</div>
  </div>
</div>

<div class="feat-card">
  <img src="{{ '/assets/img/featured/nisar_offsets.jpg' | relative_url }}" alt="Five NISAR pixel-offset displacement maps over the Bhote Koshi avalanche source, June to August 2026" loading="lazy">
  <div class="feat-body">
    <div class="feat-kicker">NISAR · satellite radar · 2026</div>
    <h3>Can NISAR see an ice–rock avalanche coming?</h3>
    <p>
      On 26 August 2026 an ice–rock avalanche above the Bhote Koshi in Nepal sent a debris flow down the
      Bhote Koshi–Trishuli valley. I analysed all five NASA–ISRO NISAR L-band pixel-offset pairs spanning the event.
      The last pre-event pair shows <b>0.96 m of median downslope motion at the source in 24 days</b>,
      but no interval stands out against size-matched regions nearby, the rate does not accelerate, and
      the pair spanning the failure decorrelates. A footprint-wide screen finds the source among 101 zones
      of downslope motion, most of them glaciers. Motion at a future source is measurable before failure;
      on its own it is not diagnostic of failure.
    </p>
    <div class="feat-links">
      <a href="https://doi.org/10.5194/egusphere-2026-5462">Brief communication (EGUsphere, open discussion)</a>
      <a href="https://doi.org/10.21203/rs.3.rs-11022365/v1">Full study (Research Square)</a>
    </div>
    <div class="feat-note">Preprints, under review. Figure: NISAR L2 offsets, ascending track 098, 20 June – 31 August 2026.</div>
  </div>
</div>
</div>
