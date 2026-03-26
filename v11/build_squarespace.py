import os

embed_content = """<!--
===========================================================================
  EMILIO MOVEMENT — V11 Landing Page · Squarespace Code Block Embed
===========================================================================

  SETUP INSTRUCTIONS
  ------------------
  1. In Squarespace, add a "Code Block" to your page (or create a blank page).
  2. Paste this entire file into the Code Block.
  3. ASSETS — Upload each file to Squarespace (Settings → Advanced → File
     Storage) or any CDN, then find-replace the placeholders below:

     REPLACE_LOGO_URL            →  ../Assets/Emlio movement logo.webp
     REPLACE_HERO_VIDEO_URL      →  ../Assets/Organizations training video.mp4
     REPLACE_THESPOT_VIDEO_URL   →  ../Assets/The Spot.mp4
     REPLACE_HAPPYBODY_IMAGE_URL →  ../Assets/Happy body dojo.jpeg
     REPLACE_OUTDOOR_IMAGE_URL   →  ../Assets/Emilio-outdoor-training.JPG
     REPLACE_PRESENTATION_IMAGE_URL → ../Assets/Presentation.jpeg
     REPLACE_MASSIH_IMAGE_URL    →  ../Assets/Massih v2.jpg

  4. CONTACT FORM — Create a free form at formspree.io, copy your Form ID,
     then replace FORMSPREE_ID_HERE with it (e.g. xpwzabcd).

  5. OPTIONAL — In Page Settings → Advanced, hide Squarespace's own header
     and footer on this page for a clean full-page experience.

===========================================================================
-->

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&family=Inter:wght@400;500;600&display=swap');

/* =========================================================================
   ALL STYLES ARE SCOPED TO .em-lp TO AVOID CONFLICTS WITH SQUARESPACE
   ========================================================================= */

/* CSS Custom Properties + base wrapper */
.em-lp {
    --color-bg-dark:    #070707;
    --color-bg-black:   #000000;
    --color-bg-light:   #ffffff;
    --color-text-dark:  #121212;
    --color-text-light: #ffffff;
    --color-text-gray:  #888888;
    --color-neon:       #11df11;
    --font-heading: 'Montserrat', sans-serif;
    --font-body:    'Inter', sans-serif;
    --space-md: 2rem;
    --space-lg: 4rem;
    --space-xl: 8rem;

    font-family: var(--font-body);
    font-size: 16px;
    line-height: 1.6;
    color: var(--color-text-dark);
    background-color: var(--color-bg-light);
    -webkit-font-smoothing: antialiased;
}

/* Scoped reset */
.em-lp * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.em-lp h1,
.em-lp h2,
.em-lp h3,
.em-lp h4,
.em-lp .geometric-header {
    font-family: var(--font-heading);
    font-weight: 800;
    text-transform: uppercase;
    line-height: 1.1;
    letter-spacing: -0.03em;
}

/* -------------------------------------------------------------------------
   UTILITIES
   ------------------------------------------------------------------------- */
.em-lp .container      { width: 90%; max-width: 1200px; margin: 0 auto; }
.em-lp .narrow-container { max-width: 800px; }

.em-lp .section-dark  { background-color: var(--color-bg-dark);  color: var(--color-text-light); }
.em-lp .section-black { background-color: var(--color-bg-black); color: var(--color-text-light); }
.em-lp .section-light { background-color: var(--color-bg-light); color: var(--color-text-dark); padding: var(--space-xl) 0; }

.em-lp .text-white  { color: var(--color-text-light); }
.em-lp .text-gray   { color: var(--color-text-gray); }
.em-lp .text-neon   { color: var(--color-neon); }
.em-lp .text-center { text-align: center; }

.em-lp .mt-4  { margin-top: 1.5rem; }
.em-lp .mt-6  { margin-top: 3rem; }
.em-lp .mt-8  { margin-top: 4rem; }
.em-lp .mb-2  { margin-bottom: 0.5rem; }
.em-lp .mb-4  { margin-bottom: 1.5rem; }
.em-lp .mb-8  { margin-bottom: 4rem; }
.em-lp .pt-8  { padding-top: 4rem; }
.em-lp .pb-2  { padding-bottom: 1rem; }
.em-lp .pb-8  { padding-bottom: 4rem; }
.em-lp .font-bold { font-weight: 700; }

@media (max-width: 768px) {
    .em-lp .mt-mobile-8 { margin-top: 4rem; }
}

/* Buttons */
.em-lp .btn-neon {
    display: inline-block;
    background-color: var(--color-neon);
    color: var(--color-bg-black);
    font-family: var(--font-heading);
    font-weight: 800;
    padding: 1rem 2.5rem;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
    clip-path: polygon(0 0, 100% 0, 95% 100%, 0% 100%);
}
.em-lp .btn-neon:hover {
    background-color: var(--color-bg-light);
    color: var(--color-neon);
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(17, 223, 17, 0.2);
}

.em-lp .link-neon {
    color: var(--color-neon);
    font-family: var(--font-heading);
    font-weight: 700;
    text-decoration: none;
    letter-spacing: 0.05em;
    transition: color 0.2s ease;
}
.em-lp .link-neon:hover { color: var(--color-bg-light); }

/* -------------------------------------------------------------------------
   HERO
   ------------------------------------------------------------------------- */
.em-lp .hero {
    position: relative;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    overflow: hidden;
}

.em-lp .logo-container {
    position: absolute;
    top: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 20;
    width: 250px;
    padding: 1rem;
    background: transparent;
    mix-blend-mode: screen;
}
.em-lp .main-logo {
    width: 100%;
    height: auto;
    display: block;
    filter: invert(1) hue-rotate(180deg) brightness(1.2);
}

.em-lp .hero-video-wrapper {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 1;
}
.em-lp .hero-bg-video {
    width: 100%; height: 100%;
    object-fit: cover;
    filter: grayscale(80%) contrast(120%);
}
.em-lp .overlay-dark {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: linear-gradient(to bottom, rgba(0,0,0,0.8), rgba(0,0,0,0.6) 40%, rgba(0,0,0,0.9));
    z-index: 2;
}

.em-lp .hero-content {
    position: relative;
    z-index: 10;
    padding: 0 1rem;
    margin-top: 4rem;
}
.em-lp .hero-title {
    font-size: clamp(3rem, 7vw, 6rem);
    margin-bottom: 1.5rem;
    color: var(--color-text-light);
}
.em-lp .hero-subtitle {
    font-size: clamp(1.1rem, 2vw, 1.4rem);
    color: var(--color-text-gray);
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.em-lp .scroll-arrow {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10;
    color: var(--color-neon);
}
.em-lp .pulse { animation: em-pulseArrow 2s infinite; }

@keyframes em-pulseArrow {
    0%   { transform: translate(-50%, 0);    opacity: 0.5; }
    50%  { transform: translate(-50%, 10px); opacity: 1;   }
    100% { transform: translate(-50%, 0);    opacity: 0.5; }
}

/* -------------------------------------------------------------------------
   TWO-COLUMN LAYOUT
   ------------------------------------------------------------------------- */
.em-lp .dual-col-layout {
    display: grid;
    grid-template-columns: 1fr;
    gap: 3rem;
}
@media (min-width: 768px) {
    .em-lp .dual-col-layout {
        grid-template-columns: 1fr 1fr;
        gap: 6rem;
    }
}
.em-lp .sticky-element { position: sticky; top: 6rem; }

.em-lp .section-title  { font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1rem; }
.em-lp .accent-block   { width: 80px; height: 8px; background-color: var(--color-neon); margin-top: 1.5rem; }
.em-lp .lead-text      { font-size: clamp(1.2rem, 2vw, 1.5rem); font-weight: 600; color: var(--color-text-dark); margin-bottom: 2rem; }

.em-lp .neon-quote {
    font-family: var(--font-heading);
    font-size: 1.3rem;
    font-weight: 700;
    padding-left: 1.5rem;
    border-left: 4px solid var(--color-neon);
    margin-top: 2.5rem;
    color: var(--color-bg-dark);
}

/* -------------------------------------------------------------------------
   PROBLEEMHERKENNING
   ------------------------------------------------------------------------- */
.em-lp .section-probleem { padding: var(--space-md) 0 var(--space-lg) 0; }

.em-lp .probleem-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    margin-top: 3rem;
}
@media (min-width: 768px) {
    .em-lp .probleem-grid { grid-template-columns: repeat(3, 1fr); }
}
.em-lp .probleem-card   { padding: 2rem; height: 100%; }
.em-lp .probleem-card p { color: var(--color-text-gray); margin-top: 1rem; }

/* -------------------------------------------------------------------------
   BEWIJSBLOK
   ------------------------------------------------------------------------- */
.em-lp .bewijs-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2.5rem;
}
@media (min-width: 768px) {
    .em-lp .bewijs-grid { grid-template-columns: repeat(2, 1fr); gap: 4rem 3rem; }
}
.em-lp .bewijs-item   { position: relative; padding-left: 3.5rem; }
.em-lp .bewijs-item p { margin-top: 0.5rem; }

.em-lp .neon-number {
    position: absolute;
    left: 0; top: 0.1rem;
    font-family: var(--font-heading);
    font-size: 1.8rem;
    font-weight: 900;
    color: var(--color-neon);
    line-height: 1;
}

/* -------------------------------------------------------------------------
   SERVICES
   ------------------------------------------------------------------------- */
.em-lp .section-services { padding: var(--space-xl) 0; }

.em-lp .services-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
    margin-top: 4rem;
}
@media (min-width: 768px) {
    .em-lp .services-grid { grid-template-columns: repeat(2, 1fr); }
}

.em-lp .service-card {
    background-color: var(--color-bg-black);
    border: 1px solid #222;
    transition: all 0.3s ease;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
}
.em-lp .service-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 0%;
    height: 4px;
    background-color: var(--color-neon);
    transition: width 0.4s ease;
}
.em-lp .service-card:hover              { border-color: #444; transform: translateY(-5px); }
.em-lp .service-card:hover::after       { width: 100%; }
.em-lp .service-card:hover .hover-media { transform: scale(1.03); }

.em-lp .service-media {
    width: 100%;
    aspect-ratio: 16/9;
    overflow: hidden;
    position: relative;
}
.em-lp .hover-media {
    width: 100%; height: 100%;
    object-fit: cover;
    transition: all 0.5s ease;
}
.em-lp .service-content {
    padding: 2.5rem 2rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}
.em-lp .service-card h3 { font-size: 1.5rem; margin-bottom: 1rem; color: var(--color-text-light); }
.em-lp .service-desc    { color: var(--color-text-gray); margin-bottom: 2rem; flex-grow: 1; }

.em-lp .service-details { list-style: none; border-top: 1px solid #333; padding-top: 1rem; }
.em-lp .service-details li {
    font-size: 0.85rem;
    color: #ccc;
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
}
.em-lp .service-details li span { font-family: var(--font-heading); color: var(--color-neon); font-weight: 700; }

/* -------------------------------------------------------------------------
   LOCATIONS & PARTNERS
   ------------------------------------------------------------------------- */
.em-lp .box-border {
    border: 2px solid var(--color-bg-dark);
    padding: 2rem;
    transition: all 0.2s ease;
}
.em-lp .box-border:hover {
    box-shadow: 8px 8px 0px var(--color-neon);
    transform: translate(-4px, -4px);
}
.em-lp .flex-center { display: flex; justify-content: center; align-items: center; height: 100%; }

.em-lp .sharp-image-wrapper {
    width: 100%;
    max-width: 500px;
    border-bottom: 8px solid var(--color-neon);
    overflow: hidden;
}
.em-lp .sharp-img { width: 100%; height: auto; display: block; object-fit: contain; }

/* -------------------------------------------------------------------------
   FAQ & SOCIAL PROOF
   ------------------------------------------------------------------------- */
.em-lp .section-faq { padding: var(--space-xl) 0; }

.em-lp .social-proof-block {
    padding: 2rem;
    border: 2px solid var(--color-bg-dark);
}
.em-lp .social-proof-block blockquote { font-size: 1.2rem; line-height: 1.6; }

.em-lp .neon-list { list-style: none; }
.em-lp .neon-list li { position: relative; padding-left: 1.5rem; line-height: 1.5; }
.em-lp .neon-list li::before {
    content: '';
    position: absolute;
    left: 0; top: 0.5rem;
    width: 6px; height: 6px;
    background-color: var(--color-neon);
    border-radius: 50%;
}

.em-lp .faq-accordion { border-top: 1px solid #333; }
.em-lp .faq-item      { border-bottom: 1px solid #333; }

.em-lp .faq-question {
    width: 100%;
    text-align: left;
    background: none;
    border: none;
    padding: 1.5rem 0;
    font-family: var(--font-heading);
    color: var(--color-text-light);
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: color 0.3s ease;
}
@media (min-width: 768px) {
    .em-lp .faq-question { font-size: 1.1rem; }
}
.em-lp .faq-question:hover { color: var(--color-neon); }

.em-lp .faq-icon { color: var(--color-neon); font-size: 1.5rem; transition: transform 0.3s ease; }
.em-lp .faq-item.active .faq-icon { transform: rotate(45deg); }

.em-lp .faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.35s ease-out; }
.em-lp .faq-answer p { color: var(--color-text-gray); padding-bottom: 1.5rem; }

/* -------------------------------------------------------------------------
   CONTACT FORM
   ------------------------------------------------------------------------- */
.em-lp .section-contact { padding: var(--space-xl) 0; }

.em-lp .box-border-neon {
    border: 1px solid #333;
    padding: 3rem;
    background-color: var(--color-bg-black);
    position: relative;
}
.em-lp .box-border-neon::before {
    content: '';
    position: absolute;
    top: -2px; left: -2px; right: -2px; bottom: -2px;
    background: linear-gradient(45deg, transparent, var(--color-neon), transparent);
    z-index: -1;
    opacity: 0.3;
}

.em-lp .form-row { display: flex; flex-wrap: wrap; gap: 2rem; margin-bottom: 2rem; }
.em-lp .form-row .form-group { flex: 1 1 calc(50% - 1rem); min-width: 200px; margin-bottom: 0; }
.em-lp .form-group { margin-bottom: 2rem; }

.em-lp .stark-form label {
    display: block;
    font-family: var(--font-heading);
    font-size: 0.85rem;
    color: var(--color-neon);
    margin-bottom: 0.5rem;
}

.em-lp .stark-form input,
.em-lp .stark-form select,
.em-lp .stark-form textarea {
    width: 100%;
    background-color: transparent;
    border: none;
    border-bottom: 1px solid #444;
    padding: 1rem 0;
    color: var(--color-text-light);
    font-family: var(--font-body);
    font-size: 1rem;
    transition: all 0.3s ease;
}
.em-lp .stark-form input:focus,
.em-lp .stark-form select:focus,
.em-lp .stark-form textarea:focus {
    outline: none;
    border-bottom-color: var(--color-neon);
    box-shadow: 0 1px 0 var(--color-neon);
}
.em-lp .stark-form textarea  { resize: vertical; min-height: 120px; }
.em-lp .stark-form select    { appearance: none; cursor: pointer; }
.em-lp .stark-form select option { background-color: var(--color-bg-dark); color: var(--color-text-light); }
.em-lp .select-wrapper       { position: relative; }
.em-lp .form-submit          { width: 100%; }

/* -------------------------------------------------------------------------
   FOOTER
   ------------------------------------------------------------------------- */
.em-lp .landing-footer { padding: 2rem 0; border-top: 1px solid #1a1a1a; }
.em-lp .flex-footer    { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; }
.em-lp .footer-logo    { font-family: var(--font-heading); font-size: 1.2rem; letter-spacing: 0.05em; }
.em-lp .footer-logo span { color: var(--color-neon); }
.em-lp .footer-copyright { font-size: 0.9rem; color: var(--color-text-gray); }
</style>

<div class="em-lp">

    <main>

        <!-- HERO -->
        <header class="hero section-dark">
            <div class="logo-container">
                <img src="https://images.squarespace-cdn.com/content/695bad7e0da3646edc4b3de0/502bee57-0e1c-41d8-a417-192d8d9869ef/Emlio+movement+logo.webp?content-type=image%2Fwebp" alt="Emilio Movement Logo" class="main-logo">
            </div>

            <div class="hero-video-wrapper">
                <video autoplay loop muted playsinline class="hero-bg-video">
                    <source src="REPLACE_HERO_VIDEO_URL" type="video/mp4">
                </video>
                <div class="overlay-dark"></div>
            </div>

            <div class="hero-content">
                <h1 class="hero-title">
                    SAMENWERKING VERSTERKEN<br>DOOR HET TE <span class="text-neon">ERVAREN</span>
                </h1>
                <p class="hero-subtitle">
                    Voor teams die vastlopen in overleg, werkdruk of onderlinge dynamiek.<br>
                    Weg van vergadertafels, terug naar echt contact.
                </p>
                <div>
                    <a href="#em-contact" class="btn-neon">PLAN EEN KENNISMAKING</a>
                </div>
            </div>

            <a href="#em-intro" class="scroll-arrow pulse">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M6 9l6 6 6-6"/>
                </svg>
            </a>
        </header>

        <!-- PROBLEEMHERKENNING -->
        <section id="em-probleemherkenning" class="section-probleem section-black">
            <div class="container">
                <div class="text-center">
                    <h2 class="section-title text-white">BEKENDE PATRONEN</h2>
                    <p style="color:var(--color-text-gray);margin-top:1rem;">Veel teams praten regelmatig over samenwerking. Toch blijft de kern vaak onbesproken.</p>
                </div>
                <div class="probleem-grid pb-2">
                    <div class="probleem-card box-border-neon">
                        <h3 class="geometric-header">ENERGIELEK</h3>
                        <p>Overleggen kosten veel energie en leveren weinig concrete, blijvende beweging op.</p>
                    </div>
                    <div class="probleem-card box-border-neon">
                        <h3 class="geometric-header">ONUITGESPROKEN</h3>
                        <p>Spanningen blijven vaak onder de oppervlakte, wat de daadkracht en het vertrouwen ondermijnt.</p>
                    </div>
                    <div class="probleem-card box-border-neon">
                        <h3 class="geometric-header">FUNCTIE VS. GEVOEL</h3>
                        <p>Teams functioneren op papier, maar voelen weinig echte, rauwe verbinding met elkaar.</p>
                    </div>
                </div>
                <div class="text-center mt-6">
                    <p class="lead-text text-gray">Praten helpt tot op zekere hoogte. Maar samenwerking speelt zich niet alleen af in woorden &ndash; het zit ook in gedrag, reacties en onderlinge afstemming.</p>
                </div>
            </div>
        </section>

        <!-- INTRO -->
        <section id="em-intro" class="section-light">
            <div class="container dual-col-layout">
                <div class="col-left sticky-element">
                    <h2 class="section-title">WAT ALS SAMENWERKING<br>VOELBAAR WORDT?</h2>
                    <div class="accent-block"></div>
                </div>
                <div class="col-right">
                    <p class="lead-text">
                        Bij Emilio Movement creëren we situaties waarin teams samenwerking <strong>direct ervaren</strong>.
                        Door samen te bewegen, spelen en reflecteren ontstaat fundamenteel inzicht, zonder dat het zwaar of geforceerd wordt.
                    </p>
                    <p>
                        Beweging haalt teams uit hun hoofd en maakt de onderstroom zichtbaar: hoe mensen reageren onder
                        druk, hoe rollen vanzelf ontstaan en waar vertrouwen daadwerkelijk groeit of stokt. Omdat het
                        lichaam meedoet, garanderen we dat inzichten verankeren in de groep.
                    </p>
                    <blockquote class="neon-quote">
                        "Deze fysieke ervaringen vormen de basis voor betekenisvolle gesprekken en constructieve, duurzame verandering."
                    </blockquote>
                </div>
            </div>
        </section>

        <!-- BEWIJSBLOK -->
        <section id="em-bewijsblok" class="section-dark">
            <div class="container pt-8 pb-8">
                <div class="text-center">
                    <h2 class="section-title text-white">WAAROM DIT WERKT VOOR TEAMS</h2>
                    <p style="color:var(--color-text-gray);margin-top:1rem;">Wetenschappelijk gefundeerd. Fysiek bewezen.</p>
                </div>
                <div class="bewijs-grid mt-4">
                    <div class="bewijs-item">
                        <div class="neon-number">01</div>
                        <h3 class="geometric-header">VEILIGHEID = PRESTATIE</h3>
                        <p class="text-gray">Uit onderzoek blijkt dat teams met een hoge mate van psychologische veiligheid significant beter presteren. In internationale studies is dit de belangrijkste voorspeller van effectieve teams.</p>
                    </div>
                    <div class="bewijs-item">
                        <div class="neon-number">02</div>
                        <h3 class="geometric-header">INTERVENTIES HEBBEN EFFECT</h3>
                        <p class="text-gray">Studies naar teambuilding tonen aan dat gerichte interventies duidelijk positieve, langdurige effecten hebben op samenwerking en vertrouwen in teamprocessen.</p>
                    </div>
                    <div class="bewijs-item">
                        <div class="neon-number">03</div>
                        <h3 class="geometric-header">BEWEGING VERLAAGT SPANNING</h3>
                        <p class="text-gray">Eén sterke sessie fysieke activiteit leidt aantoonbaar tot minder spanning en stress. Een ontspannen staat maakt de weg vrij voor constructieve interactie.</p>
                    </div>
                    <div class="bewijs-item">
                        <div class="neon-number">04</div>
                        <h3 class="geometric-header">MENSEN ONTHOUDEN DOOR TE DOEN</h3>
                        <p class="text-gray">Inzichten die men zelf ervaart, worden beter onthouden en sneller toegepast dan theorie. Ervaren, reflecteren, toepassen.</p>
                    </div>
                </div>
                <div class="text-center mt-6">
                    <p class="lead-text text-neon">Daarom combineren wij beweging, spel en reflectie.</p>
                </div>
            </div>
        </section>

        <!-- SERVICES -->
        <section id="em-diensten" class="section-services section-black">
            <div class="container">
                <div class="text-center">
                    <h2 class="section-title text-white">ONS AANBOD</h2>
                    <p style="color:var(--color-text-gray);margin-top:1rem;">Ervaringsgerichte trainingen met meetbare impact.</p>
                </div>

                <div class="services-grid">
                    <article class="service-card">
                        <div class="service-media">
                            <video loop muted playsinline class="hover-media">
                                <source src="REPLACE_THESPOT_VIDEO_URL" type="video/mp4">
                            </video>
                        </div>
                        <div class="service-content">
                            <h3>TEAMKRACHT IN BEWEGING</h3>
                            <p class="service-desc">Een speelse, fysieke teambuildingactiviteit waarin we collega's uit hun patroon halen. De nadruk ligt niet op prestatie, maar op samenwerken, vertrouwen en plezier.</p>
                            <ul class="service-details">
                                <li><span>DUUR:</span> 3–4 uur | Locatie: The Spot</li>
                                <li><span>IDEAAL VOOR:</span> Teams die verbinding zoeken</li>
                            </ul>
                        </div>
                    </article>

                    <article class="service-card">
                        <div class="service-media">
                            <img src="REPLACE_HAPPYBODY_IMAGE_URL" alt="Ontladen en Verbinden" class="hover-media">
                        </div>
                        <div class="service-content">
                            <h3>ONTLADEN &amp; VERBINDEN</h3>
                            <p class="service-desc">Voor professionals die werken met spanning, emoties of zware verhalen. In een veilige setting werken we met beweging en bokselementen om spanning los te laten en veerkracht te bouwen.</p>
                            <ul class="service-details">
                                <li><span>DUUR:</span> 3–4 uur | Locatie: Happy Body Dojo</li>
                                <li><span>IDEAAL VOOR:</span> Zorg, psychologen, coaches</li>
                            </ul>
                        </div>
                    </article>

                    <article class="service-card">
                        <div class="service-media">
                            <img src="REPLACE_OUTDOOR_IMAGE_URL" alt="Maatwerk Teambuilding" class="hover-media">
                        </div>
                        <div class="service-content">
                            <h3>MAATWERK TEAMBUILDING</h3>
                            <p class="service-desc">Gerichte interventies voor leiderschap en complexe groepsdynamiek. Elke oefening wordt afgestemd op de specifieke, strategische doelen van jullie team.</p>
                            <ul class="service-details">
                                <li><span>DOEL:</span> Specifieke knelpunten oplossen</li>
                                <li><span>RESULTAAT:</span> Direct toepasbare inzichten</li>
                            </ul>
                        </div>
                    </article>

                    <article class="service-card">
                        <div class="service-media">
                            <img src="REPLACE_PRESENTATION_IMAGE_URL" alt="Traject op Maat" class="hover-media">
                        </div>
                        <div class="service-content">
                            <h3>TRAJECT OP MAAT</h3>
                            <p class="service-desc">De structurele aanpak voor bedrijfsvitaliteit. Een intensief groeitraject waarin we fysieke sessies combineren met strategische reflectie voor blijvende gedragsverandering.</p>
                            <ul class="service-details">
                                <li><span>VORM:</span> Training &amp; Integratie</li>
                                <li><span>DUUR:</span> Duurzame commitment</li>
                            </ul>
                        </div>
                    </article>
                </div>
            </div>
        </section>

        <!-- LOCATIONS & PARTNERS -->
        <section id="em-locaties" class="section-light">
            <div class="container dual-col-layout">
                <div class="col-left">
                    <h2 class="section-title">BASISKAMPEN &amp;<br>EXPERTS</h2>

                    <div class="box-border" style="margin-top:2rem;">
                        <h3 class="geometric-header">HAPPY BODY DOJO</h3>
                        <p>De ultieme plek voor focus en herstel. Ontworpen voor trajecten waar teams de dagelijkse ruis volledig moeten uitschakelen om de kern te raken.</p>
                    </div>

                    <div class="box-border mt-4">
                        <h3 class="geometric-header">THE SPOT</h3>
                        <p>Onze arena voor ongekende kracht en expansie. De perfecte uitvalsbasis om het team fysiek en mentaal te laten groeien.</p>
                    </div>

                    <div class="mt-6">
                        <h3 class="geometric-header text-neon">GEZAMENLIJKE EXPERTISE</h3>
                        <p style="margin-top:1rem;">Gedreven door de samenwerking met <strong>Massih Hosseini</strong>, klinisch psycholoog en coach. Wij verbinden de intelligentie van het lichaam met de scherpte van de geest voor blijvende groepsontwikkeling.</p>
                    </div>
                </div>
                <div class="col-right flex-center">
                    <div class="sharp-image-wrapper">
                        <img src="https://images.squarespace-cdn.com/content/695bad7e0da3646edc4b3de0/b71133ea-eaba-4442-8a6e-8ac88857e10f/Massih+v2.jpg?content-type=image%2Fjpeg" alt="Massih Hosseini" class="sharp-img">
                    </div>
                </div>
            </div>
        </section>

        <!-- FAQ & SOCIAL PROOF -->
        <section id="em-faq" class="section-faq section-dark">
            <div class="container dual-col-layout">
                <div class="col-left">
                    <h2 class="section-title text-white">VOOR WIE &amp;<br>VRAGEN</h2>

                    <div class="social-proof-block mt-4">
                        <blockquote class="text-white">
                            "De sessie maakte in korte tijd zichtbaar wat we normaal lastig bespreekbaar vinden. Het gaf ons energie én compleet nieuwe inzichten in hoe we samenwerken."
                        </blockquote>
                        <p class="text-neon mt-4 font-bold">— DEELNEMER TEAMTRAINING</p>
                    </div>

                    <div class="mt-8">
                        <h3 class="geometric-header text-white mb-4">IS DIT GESCHIKT VOOR ONS?</h3>
                        <ul class="neon-list text-gray">
                            <li class="mb-2"><strong>HR-managers &amp; Teamleads</strong> die merken dat het team vastloopt of overleg weinig energie oplevert.</li>
                            <li class="mb-2"><strong>Ervaringsgericht</strong> — voor teams die openstaan voor een fysieke, actieve aanpak in plaats van theorie.</li>
                            <li><strong>Toegankelijk</strong> — geen sportieve ervaring nodig. Iedereen kan meedoen op eigen niveau.</li>
                        </ul>
                    </div>
                </div>

                <div class="col-right mt-mobile-8">
                    <div class="faq-accordion">
                        <div class="faq-item">
                            <button class="faq-question">IS DIT OOK VOOR NIET-SPORTIEVE TEAMS? <span class="faq-icon">+</span></button>
                            <div class="faq-answer"><p>Ja. De sessies zijn toegankelijk voor iedereen, ongeacht leeftijd, conditie of ervaring met sport. Het gaat niet om fysieke prestaties, maar om samenwerken en reflecteren.</p></div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-question">WAT LEVERT ZO'N SESSIE CONCREET OP? <span class="faq-icon">+</span></button>
                            <div class="faq-answer"><p>Teams krijgen inzicht in hun samenwerking, ervaren meer onderling vertrouwen en voelen nieuwe energie. Veel teams geven aan dat overleg daarna eerlijker en constructiever verloopt.</p></div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-question">IS HET ALLEEN "LEUK" OF OOK INHOUDELIJK? <span class="faq-icon">+</span></button>
                            <div class="faq-answer"><p>De sessies zijn speels, maar altijd inhoudelijk onderbouwd. Beweging en spel worden bewust ingezet om de onderlinge teamdynamiek zichtbaar te maken.</p></div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-question">HOE VEILIG IS DIT BIJ SPANNINGEN OF EMOTIES? <span class="faq-icon">+</span></button>
                            <div class="faq-answer"><p>Veiligheid staat altijd voorop. De sessies worden (indien nodig) begeleid door een psycholoog. Er is rigoureuze aandacht voor grenzen en tempo.</p></div>
                        </div>
                        <div class="faq-item">
                            <button class="faq-question">PAST DIT BINNEN EEN HR- OF ONTWIKKELBELEID? <span class="faq-icon">+</span></button>
                            <div class="faq-answer"><p>Ja. Veel HR-managers gebruiken dit als fundering voor teamontwikkeling, duurzame inzetbaarheid of welzijnsbeleid.</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- CONTACT FORM -->
        <section id="em-contact" class="section-contact section-black">
            <div class="container narrow-container">
                <div class="text-center mb-8">
                    <h2 class="section-title text-white">READY TO MOVE?</h2>
                    <p style="color:var(--color-text-gray);margin-top:1rem;">Nieuwsgierig wat dit kan betekenen voor jouw team? Plan direct een kennismaking in.</p>
                </div>

                <div class="box-border-neon">
                    <form id="em-landing-form" class="stark-form" action="https://formspree.io/f/FORMSPREE_ID_HERE" method="POST">
                        <div class="form-row">
                            <div class="form-group">
                                <label for="em-name">NAAM</label>
                                <input type="text" id="em-name" name="name" required placeholder="Jouw naam">
                            </div>
                            <div class="form-group">
                                <label for="em-company">ORGANISATIE</label>
                                <input type="text" id="em-company" name="company" required placeholder="Bedrijfsnaam">
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-group">
                                <label for="em-role">ROL</label>
                                <div class="select-wrapper">
                                    <select id="em-role" name="role" required>
                                        <option value="" disabled selected>Selecteer...</option>
                                        <option value="hr">HR Professional</option>
                                        <option value="founder">Oprichter / Directie</option>
                                        <option value="teamlead">Team Leader</option>
                                        <option value="other">Anders</option>
                                    </select>
                                </div>
                            </div>
                            <div class="form-group">
                                <label for="em-email">E-MAILADRES</label>
                                <input type="email" id="em-email" name="email" required placeholder="naam@bedrijf.nl">
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="em-phone">TELEFOON (OPTIONEEL)</label>
                            <input type="tel" id="em-phone" name="phone" placeholder="06 12 34 56 78">
                        </div>

                        <div class="form-group">
                            <label for="em-message">WAT IS DE GROOTSTE UITDAGING VAN HET TEAM?</label>
                            <textarea id="em-message" name="message" rows="4" required placeholder="Wees direct. Waar lopen jullie tegenaan?"></textarea>
                        </div>

                        <button type="submit" class="btn-neon form-submit mt-4">AANVRAAG VERSTUREN</button>
                    </form>
                </div>

                <div class="direct-contact text-center mt-6">
                    <a href="mailto:info@emiliomovement.nl" class="link-neon">INFO@EMILIOMOVEMENT.NL</a>
                </div>
            </div>
        </section>
    </main>

    <footer class="landing-footer section-black">
        <div class="container flex-footer">
            <div class="footer-logo">EMILIO <span>MOVEMENT</span></div>
            <div class="footer-copyright">
                &copy; <span id="year">2026</span> Emilio Movement.
            </div>
        </div>
    </footer>

</div>

<!-- REQUIRED JS FOR FAQ & REVEALS -->
<script>
document.addEventListener('DOMContentLoaded', () => {
    /* 1) FAQ Accordion */
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const btn = item.querySelector('.faq-question');
        btn.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => {
                i.classList.remove('active');
                if (i.querySelector('.faq-answer')) {
                    i.querySelector('.faq-answer').style.maxHeight = null;
                }
            });
            if (!isActive) {
                item.classList.add('active');
                const answer = item.querySelector('.faq-answer');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });
});
</script>
"""

with open(r"c:\Users\jorrin.zeebregts\AI Projects\Emiliomovement\v11\squarespace-embed.html", "w", encoding="utf-8") as f:
    f.write(embed_content)
