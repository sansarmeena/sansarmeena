// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-contact",
          title: "Contact",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/contact/";
          },
        },{id: "nav-news",
          title: "News",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/information/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-research",
          title: "Research",
          description: "AI and Earth observation for geohazards",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-memories",
          title: "Memories",
          description: "Conferences, institutional visits and fieldwork, from EGU and AGU to the Alps and the Himalaya.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/memories/";
          },
        },{id: "news-defended-my-phd-in-applied-geoinformatics-at-the-university-of-salzburg-z-gis-mortar-board",
          title: 'Defended my PhD in Applied Geoinformatics at the University of Salzburg (Z_GIS). :mortar_board:...',
          description: "",
          section: "News",},{id: "news-our-globally-distributed-landslide-training-set-hr-gldd-is-out-in-earth-system-science-data",
          title: 'Our globally distributed landslide training set HR-GLDD is out in Earth System Science...',
          description: "",
          section: "News",},{id: "news-global-landslide-mapping-using-u-net-with-diverse-backbones-across-multi-regional-and-multi-sensor-data-is-published-in-frontiers-in-earth-science",
          title: 'Global landslide mapping using U-Net with diverse backbones across multi-regional and multi-sensor data...',
          description: "",
          section: "News",},{id: "news-joined-the-geophysics-department-of-ogs-trieste-as-principal-investigator-of-the-fis-funded-natura-project-sparkles",
          title: 'Joined the Geophysics Department of OGS, Trieste, as Principal Investigator of the FIS-funded...',
          description: "",
          section: "News",},{id: "news-new-eartharxiv-preprint-with-xiaochuan-tang-and-filippo-catani-masked-autoencoding-outperforms-joint-embedding-prediction-for-frozen-probe-very-high-resolution-landslide-segmentation-with-foundation-models-trained-on-4-85-million-aerial-patches",
          title: 'New EarthArXiv preprint with Xiaochuan Tang and Filippo Catani: masked autoencoding outperforms joint-embedding...',
          description: "",
          section: "News",},{id: "news-released-open-weights-for-the-two-867m-parameter-chronosat-encoders-mae-and-jepa-on-zenodo-cc-by-4-0-rocket",
          title: 'Released open weights for the two 867M-parameter ChronoSat encoders (MAE and JEPA) on...',
          description: "",
          section: "News",},{id: "news-full-nisar-study-posted-on-research-square-nisar-offsets-measure-pre-failure-motion-but-do-not-single-out-the-bhote-koshi-avalanche-source",
          title: 'Full NISAR study posted on Research Square: NISAR offsets measure pre-failure motion but...',
          description: "",
          section: "News",},{id: "news-new-preprint-on-egusphere-nisar-pixel-offsets-measure-but-do-not-statistically-resolve-pre-failure-motion-at-the-26-august-2026-bhote-koshi-ice-rock-avalanche-nepal",
          title: 'New preprint on EGUsphere: NISAR pixel offsets measure but do not statistically resolve...',
          description: "",
          section: "News",},{id: "news-included-in-the-2026-edition-of-the-stanford-university-elsevier-list-of-the-world-s-top-2-most-cited-scientists-single-year-impact-trophy",
          title: 'Included in the 2026 edition of the Stanford University–Elsevier list of the world’s...',
          description: "",
          section: "News",},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
