import os
import re

legacy_file = 'legacy_html_version/index.html'

with open(legacy_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if css_match:
    with open('src/index.css', 'w', encoding='utf-8') as f:
        f.write(css_match.group(1).strip())
    print("CSS extracted to src/index.css")

# Extract JS
js_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if js_match:
    with open('src/legacy.js', 'w', encoding='utf-8') as f:
        f.write(js_match.group(1).strip())
    print("JS extracted to src/legacy.js")
