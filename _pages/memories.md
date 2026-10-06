---
layout: page
permalink: /memories/
title: Memories
description: Conferences, institutional visits and fieldwork, from EGU and AGU to the Alps and the Himalaya.
nav: true
nav_order: 3
images:
  photoswipe: true
---

<style>
  .mem-filters { display: flex; flex-wrap: wrap; gap: .5rem; margin: 0 0 1.5rem; }
  .mem-filters button {
    border: 1px solid var(--global-divider-color); background: transparent; color: var(--global-text-color);
    border-radius: 999px; padding: .2rem .9rem; font-size: .9rem; cursor: pointer;
  }
  .mem-filters button.active { background: var(--global-theme-color); border-color: var(--global-theme-color); color: #fff; }
  .mem-year { margin-top: 2rem; }
  .mem-event { margin: 0 0 2rem; }
  .mem-event h3 { font-size: 1.15rem; margin-bottom: .15rem; }
  .mem-meta { color: var(--global-text-color-light); font-size: .85rem; margin-bottom: .35rem; }
  .mem-meta a { color: var(--global-text-color-light); text-decoration: underline; }
  .mem-caption { margin-bottom: .6rem; }
  .mem-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 6px; }
  .mem-grid a { display: block; overflow: hidden; border-radius: 4px; aspect-ratio: 4 / 3; }
  .mem-grid img { width: 100%; height: 100%; object-fit: cover; transition: transform .2s; }
  .mem-grid a:hover img { transform: scale(1.04); }
  .mem-tag { display: inline-block; font-size: .7rem; text-transform: uppercase; letter-spacing: .04em;
    border: 1px solid var(--global-divider-color); border-radius: 3px; padding: 0 .35rem; margin-right: .4rem; }
</style>

<div class="mem-filters" role="group" aria-label="Filter memories">
  <button class="active" data-filter="all">All</button>
  <button data-filter="conference">Conferences</button>
  <button data-filter="visit">Visits</button>
  <button data-filter="fieldwork">Fieldwork</button>
  <button data-filter="award">Awards</button>
</div>

{% assign by_year = site.data.memories | group_by: "year" %}
{% for group in by_year %}

<section class="mem-year" data-year="{{ group.name }}">
  <h2>{{ group.name }}</h2>
  {% for ev in group.items %}
  <div class="mem-event" data-category="{{ ev.category }}">
    <h3>{{ ev.title }}</h3>
    <div class="mem-meta">
      <span class="mem-tag">{{ ev.category }}</span>{% if ev.place != "" %}{{ ev.place }} · {% endif %}{{ ev.date | date: "%B %Y" }}
      {% for url in ev.linkedin %} · <a href="{{ url }}">LinkedIn post</a>{% endfor %}
    </div>
    <div class="mem-caption">{{ ev.caption }}</div>
    <div class="mem-grid pswp-gallery">
      {% for ph in ev.photos %}
      <a href="{{ '/assets/memories/' | append: ph.file | append: '.jpg' | relative_url }}" data-pswp-width="{{ ph.w }}" data-pswp-height="{{ ph.h }}" data-cropped="true">
        <img src="{{ '/assets/memories/' | append: ph.file | append: '-thumb.jpg' | relative_url }}" alt="{{ ev.title }}, photo {{ forloop.index }}" loading="lazy">
      </a>
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</section>
{% endfor %}

<script>
  document.querySelectorAll(".mem-filters button").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".mem-filters button").forEach((b) => b.classList.toggle("active", b === btn));
      const f = btn.dataset.filter;
      document.querySelectorAll(".mem-event").forEach((ev) => {
        ev.style.display = f === "all" || ev.dataset.category === f ? "" : "none";
      });
      document.querySelectorAll(".mem-year").forEach((y) => {
        const visible = [...y.querySelectorAll(".mem-event")].some((ev) => ev.style.display !== "none");
        y.style.display = visible ? "" : "none";
      });
    });
  });
</script>
