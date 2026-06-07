import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.samana.name": "Samaná",
    "tour.samana.badge": "RECOMENDADO",
    "tour.samana.location": "Samaná",
    "tour.samana.note": "Niños hasta 11 años tienen precio especial",
    "tour.samana.f1": "Transporte terrestre",
    "tour.samana.f2": "Transporte marítimo",
    "tour.samana.f3": "Paseo a caballo",
    "tour.samana.f4": "Visita Cascada del Limón",
    "tour.samana.f5": "Visita pueblo de Samaná",
    "tour.samana.f6": "Visita Cayo Levantado",
    "tour.samana.f7": "Santuario de ballenas",
    "tour.samana.f8": "Visitas casitas típicas",
    "tour.samana.f9": "Desayuno y almuerzo",
    "tour.samana.f10": "Barra libre bebidas",
    "tour.samana.f11": "Guía Nacionales",
}

data_en = {
    "tour.samana.name": "Samaná",
    "tour.samana.badge": "RECOMMENDED",
    "tour.samana.location": "Samaná",
    "tour.samana.note": "Children under the age of 11 have a special price",
    "tour.samana.f1": "Ground transportation",
    "tour.samana.f2": "Marine transport",
    "tour.samana.f3": "Horse ride",
    "tour.samana.f4": "Visit Cascada del Limón",
    "tour.samana.f5": "Visit Samana town",
    "tour.samana.f6": "Visit Cayo Levantado",
    "tour.samana.f7": "Whale sanctuary",
    "tour.samana.f8": "Visit typical houses",
    "tour.samana.f9": "Breakfast and lunch",
    "tour.samana.f10": "Open bar drinks",
    "tour.samana.f11": "National Guide",
}

data_pt = {
    "tour.samana.name": "Samaná",
    "tour.samana.badge": "RECOMENDADO",
    "tour.samana.location": "Samaná",
    "tour.samana.note": "Crianças até aos 11 anos têm um preço especial",
    "tour.samana.f1": "Transporte terrestre",
    "tour.samana.f2": "Transporte marítimo",
    "tour.samana.f3": "Passeio a cavalo",
    "tour.samana.f4": "Visite Cascada del Limón",
    "tour.samana.f5": "Visite a cidade de Samana",
    "tour.samana.f6": "Visite Cayo Levantado",
    "tour.samana.f7": "Santuário de baleias",
    "tour.samana.f8": "Visite casas típicas",
    "tour.samana.f9": "Café da manhã e almoço",
    "tour.samana.f10": "Bebidas de bar aberto",
    "tour.samana.f11": "Guia nacional",
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
            id="funpark"
            img="img/buggy.png" 
            badgeKey="tour.funpark.badge"
            nameKey="tour.funpark.name"
            locationKey="tour.funpark.location"
            noteKey="tour.funpark.note"
            featuresKeys={[
              'tour.funpark.f1', 
              'tour.funpark.f2', 
              'tour.funpark.f3', 
              'tour.funpark.f4',
              'tour.funpark.f5',
              'tour.funpark.f6',
              'tour.funpark.f7',
              'tour.funpark.f8',
              'tour.funpark.f9'
            ]}
            delay="d2"
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="funpark"
            img="img/buggy.png" 
            badgeKey="tour.funpark.badge"
            nameKey="tour.funpark.name"
            locationKey="tour.funpark.location"
            noteKey="tour.funpark.note"
            featuresKeys={[
              'tour.funpark.f1', 
              'tour.funpark.f2', 
              'tour.funpark.f3', 
              'tour.funpark.f4',
              'tour.funpark.f5',
              'tour.funpark.f6',
              'tour.funpark.f7',
              'tour.funpark.f8',
              'tour.funpark.f9'
            ]}
            delay="d2"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Samana tour")
