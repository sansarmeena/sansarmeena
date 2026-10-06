---
layout: page
permalink: /research/
title: Research
description: AI and Earth observation for geohazards
nav: true
nav_order: 2
---

<p style="text-align:justify;">
  Landslides, floods and other slope and river hazards leave a clear footprint in satellite
  data, but turning that footprint into maps that responders and planners can use has
  traditionally meant weeks of manual interpretation. My research builds methods that shorten
  this path with <u>artificial intelligence</u>: deep-learning models that map hazards directly
  from optical and radar imagery, Earth-observation foundation models pre-trained on millions of
  unlabelled images, machine-learning models that say where the next failures are likely, and
  open datasets and weights that let these models be tested outside the places they were
  trained. Alongside the AI work, I use satellite radar, from Sentinel-1 to the new NISAR
  mission, to measure how slopes move before and after they fail.
</p>

#### NATURA: natural and anthropogenic drivers of landslide risk

<p style="text-align:justify;">
  <a href="https://www.ogs.it/en/projects/natura">NATURA</a> is the project I lead at OGS, funded by
  a Starting Grant of the Italian Science Fund (FIS 3, MUR) from April 2026 to March 2031. It
  brings physically-based slope modelling, AI-driven analysis of satellite data (Sentinel-2,
  PlanetScope, Copernicus DEM) and socio-economic risk analysis into one framework. The aim is
  to capture the feedbacks between landslides and human-driven landscape change: NATURA uses
  CORDEX climate projections and Shared Socioeconomic Pathways to ask how urban expansion,
  economic change and climate change will shift landslide susceptibility, and which
  communities end up most exposed. Planned outputs are high-resolution risk maps,
  socio-economic vulnerability assessments and scenario-based risk projections for disaster
  risk reduction and climate adaptation.
</p>

#### Foundation models for Earth observation

<p style="text-align:justify;">
  Labelled landslide maps are slow and expensive to make, while aerial and satellite archives hold
  decades of unlabelled imagery. I work on self-supervised foundation models that learn from those
  archives first and need few labels afterwards. In the <b>ChronoSat</b> study with Xiaochuan Tang and
  Filippo Catani, we trained a masked autoencoder (MAE) and a joint-embedding predictive variant
  (JEPA) from scratch on 4.85 million unlabelled 0.2 m aerial patches of Emilia-Romagna (1976–2023)
  and compared them for landslide segmentation under an identical frozen-encoder protocol. MAE
  outperformed JEPA at every label fraction from 1 % to 100 % under that protocol, even though
  JEPA-style objectives often win on natural-image benchmarks, which suggests the fine morphology of scarps and deposits is better
  kept by masked reconstruction. An end-to-end fine-tuned supervised SegFormer-B2 remains the stronger
  reference. A revised version of the paper is in preparation.
  <a href="https://doi.org/10.31223/X56N4B">Preprint</a> ·
  <a href="https://doi.org/10.5281/zenodo.22046362">open MAE and JEPA weights (867 M parameters each)</a>.
</p>

<div class="row justify-content-center mt-2 mb-3">
  <div class="col-sm-10">
    {% include figure.liquid loading="lazy" path="assets/img/featured/chronosat_mae_jepa.jpg" class="img-fluid rounded z-depth-1" alt="Landslide segmentation on 0.2 m aerial images: image, ground truth, MAE and JEPA predictions" %}
  </div>
</div>
<div class="caption">
  Frozen-probe landslide segmentation on 0.2 m aerial images: MAE and JEPA predictions against the ground truth, green = correct, red = false alarm (Meena, Tang and Catani, preprint).
</div>

#### Rapid landslide mapping with deep learning

<p style="text-align:justify;">
  After an earthquake or an extreme rainfall event, the first question is where the slopes
  failed. I develop and benchmark convolutional and attention-based networks that delineate
  landslides from very-high-resolution optical and SAR imagery within hours of image
  acquisition, and study how well they transfer to new regions and sensors.
  Examples: rapid mapping in the <a href="https://doi.org/10.1007/s10346-020-01602-4">Western Ghats</a>,
  <a href="https://doi.org/10.3390/rs14061449">SAR-based mapping with attention U-Net</a>, and the
  globally distributed training set <a href="https://doi.org/10.5194/essd-15-3283-2023">HR-GLDD</a>
  with its <a href="https://doi.org/10.3389/feart.2025.1710586">multi-region, multi-sensor benchmark</a>.
</p>

#### Landslide susceptibility and risk

<p style="text-align:justify;">
  Mapping past landslides is only half of the problem. I work on susceptibility models that
  combine terrain, geology, land cover and triggering factors, with attention to which inputs
  actually matter and how the choice of mapping unit and training samples changes the answer
  (<a href="https://doi.org/10.5194/nhess-22-1395-2022">Belluno, NE Italy</a>;
  <a href="https://doi.org/10.1007/s10064-025-04270-7">hybrid machine-learning classifiers</a>).
</p>

#### Slope motion from satellite radar and NISAR

<p style="text-align:justify;">
  Before many slopes fail, they creep. I use InSAR and radar offset tracking to measure this
  motion and to test what current missions can and cannot resolve, from
  <a href="https://doi.org/10.1007/s10346-023-02104-9">displacement forecasting with deep learning</a>
  to the first NISAR analyses of a Himalayan failure. For the 26 August 2026 Bhote Koshi ice–rock
  avalanche in Nepal, I processed all five NISAR L-band pixel-offset pairs spanning the event, with
  ASF's official offsets and an independent GAMMA chain. The source was moving before it failed,
  about 0.96 m in the last 24-day pre-event pair, but no interval stands out statistically against
  size-matched regions nearby and the rate does not accelerate. The honest answer to "can NISAR see
  it coming?" is therefore: it measures the motion, but that motion alone does not single out the
  slope that will fail.
  <a href="https://doi.org/10.5194/egusphere-2026-5462">Brief communication (EGUsphere)</a> ·
  <a href="https://doi.org/10.21203/rs.3.rs-11022365/v1">full study (Research Square)</a>.
</p>

<div class="row justify-content-center mt-2 mb-3">
  <div class="col-sm-12">
    {% include figure.liquid loading="lazy" path="assets/img/featured/nisar_offsets.jpg" class="img-fluid rounded z-depth-1" alt="NISAR pixel-offset displacement over the avalanche source for five intervals" %}
  </div>
</div>
<div class="caption">
  NISAR L2 pixel offsets over the avalanche source (star), ascending track 098, 20 June – 31 August 2026. R: directional coherence of the source window / of the surrounding background.
</div>

#### Floods, exposure and cascading hazards

<p style="text-align:justify;">
  Mountain hazards rarely come alone. I also work on flood susceptibility, building-exposure
  mapping and the downstream effects of mass movements, for example the
  <a href="https://doi.org/10.1007/s11069-022-05612-4">characterisation of buildings for flood exposure</a>
  and the <a href="https://doi.org/10.1007/s12665-021-09904-z">changes in water quality after the Chamoli disaster</a>.
</p>

<p style="text-align:justify;">
  The full list of papers is on the <a href="{{ '/publications/' | relative_url }}">Publications</a> page.
</p>
