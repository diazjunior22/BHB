import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.scapepark.name": "Scape Park",
    "tour.scapepark.badge": "RECOMENDADO",
    "tour.scapepark.location": "Punta Cana",
    "tour.scapepark.note": "Niños hasta 11 años tienen precio especial",
    "tour.scapepark.f1": "Transporte ida y vuelta",
    "tour.scapepark.f2": "Ruta cultural",
    "tour.scapepark.f3": "Saltos Azules",
    "tour.scapepark.f4": "Hoyo Azul",
    "tour.scapepark.f5": "Zip Line Eco Splash o Canopy",
    "tour.scapepark.f6": "Expedición a la cueva Taina",
    "tour.scapepark.f7": "Iguanalandia",
}

data_en = {
    "tour.scapepark.name": "Scape Park",
    "tour.scapepark.badge": "RECOMMENDED",
    "tour.scapepark.location": "Punta Cana",
    "tour.scapepark.note": "Children under the age of 11 have a special price",
    "tour.scapepark.f1": "Round trip transportation",
    "tour.scapepark.f2": "Cultural route",
    "tour.scapepark.f3": "Blue jumps",
    "tour.scapepark.f4": "Blue hole",
    "tour.scapepark.f5": "Zip Line Eco Splash or Canopy",
    "tour.scapepark.f6": "Expedition to the Taino cave",
    "tour.scapepark.f7": "Iguanalandia",
}

data_pt = {
    "tour.scapepark.name": "Scape Park",
    "tour.scapepark.badge": "RECOMENDADO",
    "tour.scapepark.location": "Punta Cana",
    "tour.scapepark.note": "Crianças até aos 11 anos têm um preço especial",
    "tour.scapepark.f1": "Transporte de ida e volta",
    "tour.scapepark.f2": "Rota cultural",
    "tour.scapepark.f3": "Saltos azuis",
    "tour.scapepark.f4": "Buraco azul",
    "tour.scapepark.f5": "Tirolesa Eco Splash ou Canopy",
    "tour.scapepark.f6": "Expedição à caverna Taino",
    "tour.scapepark.f7": "Iguanalândia",
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
            id="dolphinexplorer"
            img="img/island.jpg" 
            badgeKey="tour.dolphinexplorer.badge"
            nameKey="tour.dolphinexplorer.name"
            locationKey="tour.dolphinexplorer.location"
            noteKey="tour.dolphinexplorer.note"
            featuresKeys={[
              'tour.dolphinexplorer.f1', 
              'tour.dolphinexplorer.f2', 
              'tour.dolphinexplorer.f3', 
              'tour.dolphinexplorer.f4',
              'tour.dolphinexplorer.f5',
              'tour.dolphinexplorer.f6'
            ]}
            delay="d3"
          />

          <TourCard 
            id="scapepark"
            img="img/1.jpg" 
            badgeKey="tour.scapepark.badge"
            nameKey="tour.scapepark.name"
            locationKey="tour.scapepark.location"
            noteKey="tour.scapepark.note"
            featuresKeys={[
              'tour.scapepark.f1', 
              'tour.scapepark.f2', 
              'tour.scapepark.f3', 
              'tour.scapepark.f4',
              'tour.scapepark.f5',
              'tour.scapepark.f6',
              'tour.scapepark.f7'
            ]}
            delay="d1"
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="dolphinexplorer"
            img="img/island.jpg" 
            badgeKey="tour.dolphinexplorer.badge"
            nameKey="tour.dolphinexplorer.name"
            locationKey="tour.dolphinexplorer.location"
            noteKey="tour.dolphinexplorer.note"
            featuresKeys={[
              'tour.dolphinexplorer.f1', 
              'tour.dolphinexplorer.f2', 
              'tour.dolphinexplorer.f3', 
              'tour.dolphinexplorer.f4',
              'tour.dolphinexplorer.f5',
              'tour.dolphinexplorer.f6'
            ]}
            delay="d3"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Scape Park tour")
