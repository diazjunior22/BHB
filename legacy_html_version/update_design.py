import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix encoding issues in text
replacements = {
    "RepÃºblica": "República",
    "LlÃ¡manos": "Llámanos",
    "Ãºnicas": "únicas",
    "guÃ­as": "guías",
    "autÃ©ntica": "auténtica",
    "energÃ­a": "energía",
    "aquÃ­": "aquí",
    "AÃ±os": "Años",
    "SatisfacciÃ³n": "Satisfacción",
    "MÃ¡s": "Más",
    "NiÃ±os": "Niños",
    "aÃ±os": "años",
    "marÃ­timo": "marítimo",
    "GuÃ­a": "Guía",
    "animaciÃ³n": "animación",
    "MontaÃ±a": "Montaña",
    "cafÃ©": "café",
    "VerÃ¡n": "Verán",
    "QuiÃ©nes": "Quiénes",
    "autÃ©ntico": "auténtico",
    "diseÃ±ada": "diseñada",
    "AtenciÃ³n": "Atención",
    "increÃ­ble": "increíble",
    "degustaciÃ³n": "degustación",
    "superÃ³": "superó",
    "dÃ­a": "día",
    "VolverÃ©": "Volveré",
    "paraÃ­so": "paraíso",
    "LÃ©a": "Léa",
    "ParÃ­s": "París",
    "CanadÃ¡": "Canadá",
    "caribeÃ±a": "caribeña",
    "Ãºnica": "única",
    "mÃ¡s": "más",
    "prÃ³xima": "próxima",
    "UbicaciÃ³n": "Ubicación",
    "interÃ©s": "interés",
    "CuÃ©ntanos": "Cuéntanos",
    "opciÃ³n": "opción",
    "excursÃµes": "excursões",
    "CompaÃ±Ã­a": "Compañía",
    "SÃ­guenos": "Síguenos",
    "ContÃ¡ctanos": "Contáctanos",
    "Â·": "·",
    "Â©": "©",
    "â€”": "—",
    "â”€â”€â”€": "───",
    "Ã³": "ó",
    "Ã¡": "á",
    "Ã©": "é",
    "Ã­": "í",
    "Ãº": "ú",
    "Ã±": "ñ",
    "Â¿": "¿",
    "Â¡": "¡"
}

for k, v in replacements.items():
    content = content.replace(k, v)

# Design Update 1: Header texts in white
nav_target = """    .nav a {
      font-size: 14px;
      font-weight: 500;
      color: var(--gray-500);
      position: relative;
      padding: 4px 0;
      transition: color .3s;
      white-space: nowrap;
    }

    .nav a:hover {
      color: var(--navy);
    }"""
nav_replacement = """    .header:not(.scrolled) .nav a { color: var(--white); }
    .header:not(.scrolled) .nav a:hover { color: var(--cyan); }
    
    .nav a {
      font-size: 14px;
      font-weight: 500;
      color: var(--gray-500);
      position: relative;
      padding: 4px 0;
      transition: color .3s;
      white-space: nowrap;
    }

    .nav a:hover {
      color: var(--navy);
    }"""
content = content.replace(nav_target, nav_replacement)

# Design Update 2: Reservar button electric blue
btn_target = """    .btn-nav {
      background: var(--navy);
      color: var(--white) !important;
      padding: 10px 28px !important;"""
btn_replacement = """    .btn-nav {
      background: #0055ff;
      color: var(--white) !important;
      padding: 10px 28px !important;"""
content = content.replace(btn_target, btn_replacement)

# Design Update 3: Hero gradient
bg_target = """    .hero-bg {
      position: absolute;
      inset: 0;
      background:
        linear-gradient(to bottom, rgba(0, 12, 59, .55) 0%, rgba(0, 12, 59, .35) 50%, rgba(0, 12, 59, .7) 100%),
        url('img/hero.jpg') center / cover no-repeat;
      pointer-events: none;
    }"""
bg_replacement = """    .hero-bg {
      position: absolute;
      inset: 0;
      background:
        linear-gradient(135deg, rgba(0, 12, 59, 0.85) 0%, rgba(0, 188, 212, 0.3) 50%, rgba(0, 12, 59, 0.9) 100%),
        url('img/hero.jpg') center / cover no-repeat;
      pointer-events: none;
    }"""
content = content.replace(bg_target, bg_replacement)

# Design Update 4: Hero title (Caribe in white instead of cyan)
title_target = """Descubre el<br>
        <span class="hl-cyan">Caribe</span> como<br>
        <span class="hl-yellow">nunca antes</span>"""
title_replacement = """Descubre el<br>
        Caribe como<br>
        <span class="hl-yellow">nunca antes</span>"""
content = content.replace(title_target, title_replacement)

title_js_target = "'hero.title': 'Descubre el<br><span class=\"hl-cyan\">Caribe</span> como<br><span class=\"hl-yellow\">nunca antes</span>',"
title_js_replacement = "'hero.title': 'Descubre el<br>Caribe como<br><span class=\"hl-yellow\">nunca antes</span>',"
content = content.replace(title_js_target, title_js_replacement)

# Design Update 5: Hero subtext
sub_target_js = "'hero.sub': 'Excursiones premium · Todo incluido',"
sub_replacement_js = "'hero.sub': 'EXCURSIONES PREMIUM · TODO INCLUIDO',"
content = content.replace(sub_target_js, sub_replacement_js)

sub_target_html = "Excursiones premium · Todo incluido</div>"
sub_replacement_html = "EXCURSIONES PREMIUM · TODO INCLUIDO</div>"
content = content.replace(sub_target_html, sub_replacement_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully")
