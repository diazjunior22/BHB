import os
import re

legacy_file = 'legacy_html_version/index.html'
with open(legacy_file, 'r', encoding='utf-8') as f:
    html = f.read()

def html_to_jsx(content):
    c = content.replace('class="', 'className="')
    c = c.replace('class=\'', 'className=\'')
    c = c.replace('for="', 'htmlFor="')
    c = c.replace('tabindex="', 'tabIndex="')
    c = c.replace('viewbox="', 'viewBox="')
    c = c.replace('stroke-width', 'strokeWidth')
    c = c.replace('stroke-linecap', 'strokeLinecap')
    c = c.replace('stroke-linejoin', 'strokeLinejoin')
    c = c.replace('fill-rule', 'fillRule')
    c = c.replace('clip-rule', 'clipRule')
    # Close img tags
    c = re.sub(r'(<img[^>]+)(?<!/)>', r'\1 />', c)
    # Close input tags
    c = re.sub(r'(<input[^>]+)(?<!/)>', r'\1 />', c)
    # Close br tags
    c = re.sub(r'(<br[^>]*)(?<!/)>', r'<br />', c)
    # Handle style strings
    c = re.sub(r'style="([^"]+)"', r'style={{ /* \1 */ }}', c) # manual fix needed later
    
    # Replace data-i18n attributes with t() hook calls
    # E.g. <span data-i18n="nav.tours">Tours</span> -> <span>{t('nav.tours')}</span>
    c = re.sub(r'<([a-zA-Z0-9]+)([^>]*) data-i18n="([^"]+)"([^>]*)>(.*?)</\1>', r'<\1\2\4>{t("\3")}</\1>', c)
    c = re.sub(r'<([a-zA-Z0-9]+)([^>]*) data-i18n-html="([^"]+)"([^>]*) dangerouslySetInnerHTML=\{\{ __html: t\("\3"\) \}\}></\1>', r'<\1\2\4 dangerouslySetInnerHTML={{ __html: t("\3") }}></\1>', c)
    
    # For tags with data-i18n-html that weren't caught
    c = re.sub(r'<([a-zA-Z0-9]+)([^>]*) data-i18n-html="([^"]+)"([^>]*)>(.*?)</\1>', r'<\1\2\4 dangerouslySetInnerHTML={{ __html: t("\3") }}></\1>', c)

    return c

# Create components directory
os.makedirs('src/components', exist_ok=True)

def write_component(name, content, extra_imports=""):
    jsx = html_to_jsx(content)
    code = f"""import React from 'react';
import {{ useTranslation }} from '../I18nContext';
{extra_imports}

const {name} = () => {{
  const {{ t }} = useTranslation();
  return (
    <>
{jsx}
    </>
  );
}};

export default {name};
"""
    with open(f'src/components/{name}.jsx', 'w', encoding='utf-8') as f:
        f.write(code)

# Header
header_match = re.search(r'<header[^>]*>.*?</header>', html, re.DOTALL)
if header_match: write_component('Header', header_match.group(0))

# Hero
hero_match = re.search(r'<div class="hero".*?<!-- ─── ABOUT ─── -->', html, re.DOTALL)
if hero_match: 
    # trim the comment
    h = hero_match.group(0).split('<!-- ───')[0].strip()
    write_component('Hero', h)

# Tours
# I will create ToursGrid component manually to handle the new Santo Domingo tour properly
# So I'll just write a basic one here and overwrite it later if needed

# About
about_match = re.search(r'<section class="section about".*?</section>', html, re.DOTALL)
if about_match: write_component('About', about_match.group(0))

# Testimonials
test_match = re.search(r'<section class="section testimonials".*?</section>', html, re.DOTALL)
if test_match: write_component('Testimonials', test_match.group(0))

# Contact
contact_match = re.search(r'<section class="section contact".*?</section>', html, re.DOTALL)
if contact_match: write_component('Contact', contact_match.group(0))

# Footer
footer_match = re.search(r'<footer.*?</footer>', html, re.DOTALL)
if footer_match: write_component('Footer', footer_match.group(0))

# Main App
app_code = """import React from 'react';
import { I18nProvider } from './I18nContext';
import Header from './components/Header';
import Hero from './components/Hero';
import ToursGrid from './components/ToursGrid';
import About from './components/About';
import Testimonials from './components/Testimonials';
import Contact from './components/Contact';
import Footer from './components/Footer';

function App() {
  return (
    <I18nProvider>
      <Header />
      <main>
        <Hero />
        <ToursGrid />
        <About />
        <Testimonials />
        <Contact />
      </main>
      <Footer />
    </I18nProvider>
  );
}

export default App;
"""
with open('src/App.jsx', 'w', encoding='utf-8') as f:
    f.write(app_code)

print("Components generated")
