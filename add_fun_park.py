import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.funpark.name": "Fun Park 4x1",
    "tour.funpark.badge": "RECOMENDADO",
    "tour.funpark.location": "Punta Cana",
    "tour.funpark.note": "Niños hasta 11 años tienen precio especial",
    "tour.funpark.f1": "Transporte ida y vuelta",
    "tour.funpark.f2": "ZipLine o Canopy",
    "tour.funpark.f3": "Booguie Doble o familiar",
    "tour.funpark.f4": "ECO Safari",
    "tour.funpark.f5": "Paseo a caballo",
    "tour.funpark.f6": "Playa Macao",
    "tour.funpark.f7": "Comida típica dominicana",
    "tour.funpark.f8": "Bebidas NO alcohólicas",
    "tour.funpark.f9": "Equipos de seguridad",
}

data_en = {
    "tour.funpark.name": "Fun Park 4x1",
    "tour.funpark.badge": "RECOMMENDED",
    "tour.funpark.location": "Punta Cana",
    "tour.funpark.note": "Children under the age of 11 have a special price",
    "tour.funpark.f1": "Round trip transportation",
    "tour.funpark.f2": "Zip Line or Canopy",
    "tour.funpark.f3": "Double or Family Boogie",
    "tour.funpark.f4": "Eco safari",
    "tour.funpark.f5": "Horse ride",
    "tour.funpark.f6": "Macau beach",
    "tour.funpark.f7": "Typical dominican food",
    "tour.funpark.f8": "Non-alcoholic beverages",
    "tour.funpark.f9": "Security equipments",
}

data_pt = {
    "tour.funpark.name": "Fun Park 4x1",
    "tour.funpark.badge": "RECOMENDADO",
    "tour.funpark.location": "Punta Cana",
    "tour.funpark.note": "Crianças até aos 11 anos têm um preço especial",
    "tour.funpark.f1": "Transporte de ida e volta",
    "tour.funpark.f2": "Tirolesa ou Canopy",
    "tour.funpark.f3": "Booguie duplo ou familiar",
    "tour.funpark.f4": "Safári ecológico",
    "tour.funpark.f5": "Passeio a cavalo",
    "tour.funpark.f6": "Praia de Macau",
    "tour.funpark.f7": "Comida típica dominicana",
    "tour.funpark.f8": "Bebidas não alcoólicas",
    "tour.funpark.f9": "Equipamentos de segurança",
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
            id="pescafishing"
            img="img/catamaran.png" 
            badgeKey="tour.pescafishing.badge"
            nameKey="tour.pescafishing.name"
            locationKey="tour.pescafishing.location"
            noteKey="tour.pescafishing.note"
            featuresKeys={[
              'tour.pescafishing.f1', 
              'tour.pescafishing.f2', 
              'tour.pescafishing.f3', 
              'tour.pescafishing.f4',
              'tour.pescafishing.f5',
              'tour.pescafishing.f6',
              'tour.pescafishing.f7'
            ]}
            delay="d1"
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="pescafishing"
            img="img/catamaran.png" 
            badgeKey="tour.pescafishing.badge"
            nameKey="tour.pescafishing.name"
            locationKey="tour.pescafishing.location"
            noteKey="tour.pescafishing.note"
            featuresKeys={[
              'tour.pescafishing.f1', 
              'tour.pescafishing.f2', 
              'tour.pescafishing.f3', 
              'tour.pescafishing.f4',
              'tour.pescafishing.f5',
              'tour.pescafishing.f6',
              'tour.pescafishing.f7'
            ]}
            delay="d1"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Fun Park tour")
