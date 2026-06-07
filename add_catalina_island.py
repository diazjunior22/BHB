import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.catalinaisland.name": "Catalina Island",
    "tour.catalinaisland.badge": "RECOMENDADO",
    "tour.catalinaisland.location": "Punta Cana",
    "tour.catalinaisland.note": "Niños hasta 11 años tienen precio especial",
    "tour.catalinaisland.f1": "Transporte terrestre",
    "tour.catalinaisland.f2": "Transporte marítimo",
    "tour.catalinaisland.f3": "Equipo de Snorkel",
    "tour.catalinaisland.f4": "VISITA al banco de peces",
    "tour.catalinaisland.f5": "Almuerzo tipo buffet",
    "tour.catalinaisland.f6": "Barra libre de bebidas alcohólicas y NO alcohólicas",
    "tour.catalinaisland.f7": "Guía Oficial y animación",
}

data_en = {
    "tour.catalinaisland.name": "Catalina Island",
    "tour.catalinaisland.badge": "RECOMMENDED",
    "tour.catalinaisland.location": "Punta Cana",
    "tour.catalinaisland.note": "Children under the age of 11 have a special price",
    "tour.catalinaisland.f1": "Ground transportation",
    "tour.catalinaisland.f2": "Marine transport",
    "tour.catalinaisland.f3": "Snorkeling equipment",
    "tour.catalinaisland.f4": "VISIT to the school of fish",
    "tour.catalinaisland.f5": "Buffet-style lunch",
    "tour.catalinaisland.f6": "Open bar of alcoholic and non-alcoholic drinks",
    "tour.catalinaisland.f7": "Official guide and animation",
}

data_pt = {
    "tour.catalinaisland.name": "Catalina Island",
    "tour.catalinaisland.badge": "RECOMENDADO",
    "tour.catalinaisland.location": "Punta Cana",
    "tour.catalinaisland.note": "Crianças até aos 11 anos têm um preço especial",
    "tour.catalinaisland.f1": "Transporte terrestre",
    "tour.catalinaisland.f2": "Transporte marítimo",
    "tour.catalinaisland.f3": "Equipamento de mergulho",
    "tour.catalinaisland.f4": "VISITA ao cardume de peixes",
    "tour.catalinaisland.f5": "Almoço tipo bufê",
    "tour.catalinaisland.f6": "Bar aberto de bebidas alcoólicas e não alcoólicas",
    "tour.catalinaisland.f7": "Guia oficial e animação",
}

updates = {'es': data_es, 'en': data_en, 'pt': data_pt}

for lang, filepath in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    content.update(updates[lang])
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

# Update ToursGrid.jsx
grid_file = 'src/components/ToursGrid.jsx'
with open(grid_file, 'r', encoding='utf-8') as f:
    grid_content = f.read()

new_card = """          <TourCard 
            id="samana"
            img="img/island.jpg" 
            badgeKey="tour.samana.badge"
            nameKey="tour.samana.name"
            locationKey="tour.samana.location"
            noteKey="tour.samana.note"
            featuresKeys={[
              'tour.samana.f1', 
              'tour.samana.f2', 
              'tour.samana.f3', 
              'tour.samana.f4',
              'tour.samana.f5',
              'tour.samana.f6',
              'tour.samana.f7',
              'tour.samana.f8',
              'tour.samana.f9',
              'tour.samana.f10',
              'tour.samana.f11'
            ]}
            delay="d3"
          />

          <TourCard 
            id="catalinaisland"
            img="img/island.jpg" 
            badgeKey="tour.catalinaisland.badge"
            nameKey="tour.catalinaisland.name"
            locationKey="tour.catalinaisland.location"
            noteKey="tour.catalinaisland.note"
            featuresKeys={[
              'tour.catalinaisland.f1', 
              'tour.catalinaisland.f2', 
              'tour.catalinaisland.f3', 
              'tour.catalinaisland.f4',
              'tour.catalinaisland.f5',
              'tour.catalinaisland.f6',
              'tour.catalinaisland.f7'
            ]}
            delay="d1"
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="samana"
            img="img/island.jpg" 
            badgeKey="tour.samana.badge"
            nameKey="tour.samana.name"
            locationKey="tour.samana.location"
            noteKey="tour.samana.note"
            featuresKeys={[
              'tour.samana.f1', 
              'tour.samana.f2', 
              'tour.samana.f3', 
              'tour.samana.f4',
              'tour.samana.f5',
              'tour.samana.f6',
              'tour.samana.f7',
              'tour.samana.f8',
              'tour.samana.f9',
              'tour.samana.f10',
              'tour.samana.f11'
            ]}
            delay="d3"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Catalina Island tour")
