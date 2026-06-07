$content = Get-Content index.html -Raw -Encoding UTF8

# Fix common encoding errors
$content = $content.Replace("RepÃºblica", "República")
$content = $content.Replace("LlÃ¡manos", "Llámanos")
$content = $content.Replace("Ãºnicas", "únicas")
$content = $content.Replace("guÃ­as", "guías")
$content = $content.Replace("autÃ©ntica", "auténtica")
$content = $content.Replace("energÃ­a", "energía")
$content = $content.Replace("aquÃ­", "aquí")
$content = $content.Replace("AÃ±os", "Años")
$content = $content.Replace("SatisfacciÃ³n", "Satisfacción")
$content = $content.Replace("MÃ¡s", "Más")
$content = $content.Replace("NiÃ±os", "Niños")
$content = $content.Replace("aÃ±os", "años")
$content = $content.Replace("marÃ­timo", "marítimo")
$content = $content.Replace("GuÃ­a", "Guía")
$content = $content.Replace("animaciÃ³n", "animación")
$content = $content.Replace("MontaÃ±a", "Montaña")
$content = $content.Replace("cafÃ©", "café")
$content = $content.Replace("VerÃ¡n", "Verán")
$content = $content.Replace("QuiÃ©nes", "Quiénes")
$content = $content.Replace("autÃ©ntico", "auténtico")
$content = $content.Replace("diseÃ±ada", "diseñada")
$content = $content.Replace("AtenciÃ³n", "Atención")
$content = $content.Replace("increÃ­ble", "increíble")
$content = $content.Replace("degustaciÃ³n", "degustación")
$content = $content.Replace("superÃ³", "superó")
$content = $content.Replace("dÃ­a", "día")
$content = $content.Replace("VolverÃ©", "Volveré")
$content = $content.Replace("paraÃ­so", "paraíso")
$content = $content.Replace("LÃ©a", "Léa")
$content = $content.Replace("ParÃ­s", "París")
$content = $content.Replace("CanadÃ¡", "Canadá")
$content = $content.Replace("caribeÃ±a", "caribeña")
$content = $content.Replace("Ãºnica", "única")
$content = $content.Replace("mÃ¡s", "más")
$content = $content.Replace("prÃ³xima", "próxima")
$content = $content.Replace("UbicaciÃ³n", "Ubicación")
$content = $content.Replace("interÃ©s", "interés")
$content = $content.Replace("CuÃ©ntanos", "Cuéntanos")
$content = $content.Replace("opciÃ³n", "opción")
$content = $content.Replace("excursÃµes", "excursões")
$content = $content.Replace("CompaÃ±Ã­a", "Compañía")
$content = $content.Replace("SÃ­guenos", "Síguenos")
$content = $content.Replace("ContÃ¡ctanos", "Contáctanos")
$content = $content.Replace("Â·", "·")
$content = $content.Replace("Â©", "©")
$content = $content.Replace("â€”", "—")
$content = $content.Replace("â”€â”€â”€", "───")
$content = $content.Replace("Ã³", "ó")
$content = $content.Replace("Ã", "í") # Catch any stragglers, but carefully. Better not to globally replace single Ã unless necessary. Let's just fix the exact strings.

# Design Update 1: Header texts in white
$content = $content.Replace(
    ".nav a {",
    ".header:not(.scrolled) .nav a { color: var(--white); } .header:not(.scrolled) .nav a:hover { color: var(--cyan); } .nav a {"
)

# Design Update 2: Reservar button electric blue
$content = $content.Replace(
    "background: var(--navy);`r`n      color: var(--white) !important;`r`n      padding: 10px 28px !important;",
    "background: #0055ff;`r`n      color: var(--white) !important;`r`n      padding: 10px 28px !important;"
)

# Design Update 3: Hero gradient
$content = $content.Replace(
    "linear-gradient(to bottom, rgba(0, 12, 59, .55) 0%, rgba(0, 12, 59, .35) 50%, rgba(0, 12, 59, .7) 100%),",
    "linear-gradient(135deg, rgba(0, 12, 59, 0.85) 0%, rgba(0, 188, 212, 0.3) 50%, rgba(0, 12, 59, 0.9) 100%),"
)

# Design Update 4: Hero title (Caribe in white instead of cyan)
$content = $content.Replace(
    "Descubre el<br><span class=`"hl-cyan`">Caribe</span> como<br><span class=`"hl-yellow`">nunca antes</span>",
    "Descubre el<br>Caribe como<br><span class=`"hl-yellow`">nunca antes</span>"
)

# Design Update 5: Hero subtext
$content = $content.Replace(
    "'hero.sub': 'Excursiones premium · Todo incluido',",
    "'hero.sub': 'EXCURSIONES PREMIUM · TODO INCLUIDO',"
)

# Also fix the HTML fallback just in case
$content = $content.Replace(
    "Excursiones premium · Todo incluido</div>",
    "EXCURSIONES PREMIUM · TODO INCLUIDO</div>"
)

$utf8NoBom = New-Object System.Text.UTF8Encoding $false
[System.IO.File]::WriteAllText("index.html", $content, $utf8NoBom)
