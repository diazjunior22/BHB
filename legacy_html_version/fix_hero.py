import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix .hero height and centering
hero_target = """    .hero {
      height: 100dvh;
      height: 100svh;
      height: 100vh;
      display: flex;
      align-items: center;
      position: relative;
      background: var(--navy-deeper);
      overflow: hidden;
      perspective: 1200px;
    }"""
hero_replacement = """    .hero {
      height: 100dvh;
      min-height: 750px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
      background: var(--navy-deeper);
      overflow: hidden;
      perspective: 1200px;
    }"""
content = content.replace(hero_target, hero_replacement)

# Fix container padding
container_target = """    .hero .container {
      position: relative;
      z-index: 3;
      width: 100%;
      padding-top: 130px;
      padding-bottom: 40px;
    }"""
container_replacement = """    .hero .container {
      position: relative;
      z-index: 3;
      width: 100%;
      padding-top: 90px;
      padding-bottom: 80px;
    }"""
content = content.replace(container_target, container_replacement)

# Fix title size
title_target = """    .hero-title {
      font-size: clamp(48px, 8.5vw, 120px);
      font-weight: 700;
      line-height: .88;
      letter-spacing: -.025em;
      color: var(--white);
      margin-bottom: 12px;"""
title_replacement = """    .hero-title {
      font-size: clamp(38px, 6.5vw, 84px);
      font-weight: 700;
      line-height: .92;
      letter-spacing: -.02em;
      color: var(--white);
      margin-bottom: 16px;"""
content = content.replace(title_target, title_replacement)

# Fix sub margin
sub_target = """    .hero-sub {
      font-size: clamp(13px, 1.1vw, 17px);
      font-weight: 400;
      color: rgba(255, 255, 255, .4);
      letter-spacing: .35em;
      text-transform: uppercase;
      margin-bottom: 28px;"""
sub_replacement = """    .hero-sub {
      font-size: clamp(12px, 1vw, 15px);
      font-weight: 400;
      color: rgba(255, 255, 255, .4);
      letter-spacing: .3em;
      text-transform: uppercase;
      margin-bottom: 24px;"""
content = content.replace(sub_target, sub_replacement)

# Fix desc margin
desc_target = """    .hero-desc {
      max-width: 480px;
      font-size: clamp(15px, 1.1vw, 17px);
      line-height: 1.7;
      color: rgba(255, 255, 255, .55);
      margin-bottom: 36px;"""
desc_replacement = """    .hero-desc {
      max-width: 480px;
      font-size: clamp(14px, 1.1vw, 16px);
      line-height: 1.6;
      color: rgba(255, 255, 255, .65);
      margin-bottom: 28px;"""
content = content.replace(desc_target, desc_replacement)

# Fix stats margin & padding
stats_target = """    .hero-stats {
      display: flex;
      gap: 48px;
      margin-top: 48px;
      padding-top: 28px;
      border-top: 1px solid rgba(255, 255, 255, .05);
      backdrop-filter: blur(12px);
      background: rgba(255, 255, 255, .02);
      border-radius: 16px;
      padding: 24px 32px;"""
stats_replacement = """    .hero-stats {
      display: flex;
      gap: 32px;
      margin-top: 32px;
      backdrop-filter: blur(12px);
      background: rgba(255, 255, 255, .03);
      border-radius: 16px;
      padding: 16px 28px;"""
content = content.replace(stats_target, stats_replacement)

# Adjust scroll indicator slightly
scroll_target = """    .hero-scroll-indicator {
      position: absolute;
      bottom: 32px;"""
scroll_replacement = """    .hero-scroll-indicator {
      position: absolute;
      bottom: 24px;"""
content = content.replace(scroll_target, scroll_replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hero layout fixed")
