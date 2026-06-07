import os
import re

# Fix CSS
with open('src/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace("url('img/", "url('/img/")
css = css.replace("url(\"img/", "url(\"/img/")
css = css.replace("url(img/", "url(/img/")

with open('src/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Fix JSX
for file in os.listdir('src/components'):
    if file.endswith('.jsx'):
        with open(f'src/components/{file}', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace HTML comments with JSX comments
        content = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', content)
        
        # Replace style strings that didn't get caught
        content = re.sub(r'style="([^"]+)"', r'style={{}}', content)

        with open(f'src/components/{file}', 'w', encoding='utf-8') as f:
            f.write(content)

print("Errors fixed")
