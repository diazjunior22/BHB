import re

legacy_file = 'legacy_html_version/index.html'
react_file = 'index.html'

with open(legacy_file, 'r', encoding='utf-8') as f:
    legacy_html = f.read()

with open(react_file, 'r', encoding='utf-8') as f:
    react_html = f.read()

# Extract fonts from legacy
fonts_match = re.search(r'(<link rel="preconnect" href="https://fonts.googleapis.com">.*?<link href="https://fonts.googleapis.com/css2[^"]+" rel="stylesheet">)', legacy_html, re.DOTALL)

if fonts_match:
    fonts_str = fonts_match.group(1)
    react_html = react_html.replace('</head>', f'    {fonts_str}\n  </head>')

# Update title
react_html = react_html.replace('<title>temp_react</title>', '<title>BHB Travel & Tour</title>')

with open(react_file, 'w', encoding='utf-8') as f:
    f.write(react_html)

print("index.html updated")
