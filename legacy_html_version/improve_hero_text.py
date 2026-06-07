import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Title CSS
title_target = """    .hero-title {
      font-size: clamp(38px, 6.5vw, 84px);
      font-weight: 700;
      line-height: .92;
      letter-spacing: -.02em;
      color: var(--white);
      margin-bottom: 16px;
      opacity: 0;
      transform: translateY(30px);
      animation: heroFade .9s .35s forwards;
    }"""
title_replacement = """    .hero-title {
      font-size: clamp(42px, 7.5vw, 96px);
      font-weight: 700;
      line-height: .95;
      letter-spacing: -.01em;
      color: var(--white);
      text-shadow: 0 12px 30px rgba(0, 12, 59, 0.5);
      margin-bottom: 20px;
      opacity: 0;
      transform: translateY(30px);
      animation: heroFade .9s .35s forwards;
    }"""
content = content.replace(title_target, title_replacement)

# 2. Update Hero Sub CSS
sub_target = """    .hero-sub {
      font-size: clamp(12px, 1vw, 15px);
      font-weight: 400;
      color: rgba(255, 255, 255, .4);
      letter-spacing: .3em;
      text-transform: uppercase;
      margin-bottom: 24px;"""
sub_replacement = """    .hero-sub {
      font-size: clamp(12px, 1vw, 14px);
      font-weight: 500;
      color: var(--cyan);
      letter-spacing: .25em;
      text-transform: uppercase;
      text-shadow: 0 2px 10px rgba(0, 188, 212, 0.2);
      margin-bottom: 20px;"""
content = content.replace(sub_target, sub_replacement)

# 3. Update Hero Desc CSS
desc_target = """    .hero-desc {
      max-width: 480px;
      font-size: clamp(14px, 1.1vw, 16px);
      line-height: 1.6;
      color: rgba(255, 255, 255, .65);
      margin-bottom: 28px;"""
desc_replacement = """    .hero-desc {
      max-width: 500px;
      font-size: clamp(15px, 1.1vw, 17px);
      line-height: 1.65;
      color: rgba(255, 255, 255, 0.85);
      text-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
      margin-bottom: 36px;"""
content = content.replace(desc_target, desc_replacement)

# 4. Update the texts in HTML and JS
html_sub_old = "EXCURSIONES PREMIUM · TODO INCLUIDO</div>"
html_sub_new = "EXPERIENCIAS EXCLUSIVAS · SERVICIO VIP</div>"
content = content.replace(html_sub_old, html_sub_new)

js_sub_old = "'hero.sub': 'EXCURSIONES PREMIUM · TODO INCLUIDO',"
js_sub_new = "'hero.sub': 'EXPERIENCIAS EXCLUSIVAS · SERVICIO VIP',"
content = content.replace(js_sub_old, js_sub_new)

html_desc_old = "Vive experiencias únicas con los mejores guías, transporte, comida y la\n          auténtica energía del Caribe. Tu aventura comienza aquí.</p>"
html_desc_new = "Descubre la verdadera esencia de Punta Cana con nuestro servicio premium. Disfruta de guías expertos, atención personalizada y recuerdos inolvidables.</p>"
content = content.replace(html_desc_old, html_desc_new)
# In case the exact formatting didn't match:
content = content.replace("Vive experiencias únicas con los mejores guías, transporte, comida y la auténtica energía del Caribe. Tu aventura comienza aquí.", "Descubre la verdadera esencia de Punta Cana con nuestro servicio premium. Disfruta de guías expertos, atención personalizada y recuerdos inolvidables.")

js_desc_old = "'hero.desc': 'Vive experiencias únicas con los mejores guías, transporte, comida y la auténtica energía del Caribe. Tu aventura comienza aquí.',"
js_desc_new = "'hero.desc': 'Descubre la verdadera esencia de Punta Cana con nuestro servicio premium. Disfruta de guías expertos, atención personalizada y recuerdos inolvidables.',"
content = content.replace(js_desc_old, js_desc_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero text improved successfully")
