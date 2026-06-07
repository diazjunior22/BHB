import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.cocobongo.name": "Coco Bongo Regular",
    "tour.cocobongo.badge": "RECOMENDADO",
    "tour.cocobongo.location": "Punta Cana",
    "tour.cocobongo.note": "Transporte PRIVADO 20 dólares adicionales",
    "tour.cocobongo.f1": "DRINK PACK: Transporte + 5 Tragos Nacionales",
    "tour.cocobongo.f2": "OPEN BAR: Transporte + Barra Libre Toda la Noche",
    "tour.cocobongo.f3": "Bebidas Nacionales (Ron, Vodka, Whisky, Gin, Tequila, Cerveza)",
    "tour.cocobongo.f4": "Show espectacular en vivo y música",
}

data_en = {
    "tour.cocobongo.name": "Coco Bongo Regular",
    "tour.cocobongo.badge": "RECOMMENDED",
    "tour.cocobongo.location": "Punta Cana",
    "tour.cocobongo.note": "PRIVATE transportation 20 additional dollars",
    "tour.cocobongo.f1": "DRINK PACK: Transportation + 5 National Drinks",
    "tour.cocobongo.f2": "OPEN BAR: Transportation + Open Bar All Night",
    "tour.cocobongo.f3": "National Drinks (Rum, Vodka, Whiskey, Gin, Tequila, Beer)",
    "tour.cocobongo.f4": "Spectacular live show and music",
}

data_pt = {
    "tour.cocobongo.name": "Coco Bongo Regular",
    "tour.cocobongo.badge": "RECOMENDADO",
    "tour.cocobongo.location": "Punta Cana",
    "tour.cocobongo.note": "Transporte PRIVADO 20 dólares adicionais",
    "tour.cocobongo.f1": "DRINK PACK: Transporte + 5 Bebidas Nacionais",
    "tour.cocobongo.f2": "OPEN BAR: Transporte + Open Bar A Noite Toda",
    "tour.cocobongo.f3": "Bebidas Nacionais (Rum, Vodka, Uísque, Gin, Tequila, Cerveja)",
    "tour.cocobongo.f4": "Show espetacular ao vivo e música",
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
            id="santodomingo"
            img="img/island.jpg"
            badgeKey="tour.santodomingo.badge"
            nameKey="tour.santodomingo.name"
            locationKey="tour.santodomingo.location"
            noteKey="tour.santodomingo.note"
            featuresKeys={[
              'tour.santodomingo.f1', 'tour.santodomingo.f2', 'tour.santodomingo.f3', 
              'tour.santodomingo.f4', 'tour.santodomingo.f5', 'tour.santodomingo.f6',
              'tour.santodomingo.f7', 'tour.santodomingo.f8', 'tour.santodomingo.f9',
              'tour.santodomingo.f10', 'tour.santodomingo.f11', 'tour.santodomingo.f12'
            ]}
            delay="d3"
          />

          <TourCard 
            id="cocobongo"
            img="img/buggy.png" 
            badgeKey="tour.cocobongo.badge"
            nameKey="tour.cocobongo.name"
            locationKey="tour.cocobongo.location"
            noteKey="tour.cocobongo.note"
            featuresKeys={[
              'tour.cocobongo.f1', 
              'tour.cocobongo.f2', 
              'tour.cocobongo.f3', 
              'tour.cocobongo.f4'
            ]}
            delay="d1"
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="santodomingo"
            img="img/island.jpg"
            badgeKey="tour.santodomingo.badge"
            nameKey="tour.santodomingo.name"
            locationKey="tour.santodomingo.location"
            noteKey="tour.santodomingo.note"
            featuresKeys={[
              'tour.santodomingo.f1', 'tour.santodomingo.f2', 'tour.santodomingo.f3', 
              'tour.santodomingo.f4', 'tour.santodomingo.f5', 'tour.santodomingo.f6',
              'tour.santodomingo.f7', 'tour.santodomingo.f8', 'tour.santodomingo.f9',
              'tour.santodomingo.f10', 'tour.santodomingo.f11', 'tour.santodomingo.f12'
            ]}
            delay="d3"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Coco Bongo tour")
