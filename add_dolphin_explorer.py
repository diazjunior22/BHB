import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.dolphinexplorer.name": "Dolphin Explorer",
    "tour.dolphinexplorer.badge": "RECOMENDADO",
    "tour.dolphinexplorer.location": "Punta Cana",
    "tour.dolphinexplorer.note": "",
    "tour.dolphinexplorer.f1": "Transporte ida y vuelta",
    "tour.dolphinexplorer.f2": "VISITA aves exóticas",
    "tour.dolphinexplorer.f3": "INTERACCIÓN con León Marino",
    "tour.dolphinexplorer.f4": "INTERACCIÓN con delfines (1 hora)",
    "tour.dolphinexplorer.f5": "Lockers para guardar tus pertenencias",
    "tour.dolphinexplorer.f6": "Equipos de seguridad y guías",
}

data_en = {
    "tour.dolphinexplorer.name": "Dolphin Explorer",
    "tour.dolphinexplorer.badge": "RECOMMENDED",
    "tour.dolphinexplorer.location": "Punta Cana",
    "tour.dolphinexplorer.note": "",
    "tour.dolphinexplorer.f1": "Round trip transportation",
    "tour.dolphinexplorer.f2": "VISIT exotic birds",
    "tour.dolphinexplorer.f3": "INTERACTION with Sea Lion",
    "tour.dolphinexplorer.f4": "INTERACTION with dolphins (1 hour)",
    "tour.dolphinexplorer.f5": "Lockers to store your belongings",
    "tour.dolphinexplorer.f6": "Safety equipment and guides",
}

data_pt = {
    "tour.dolphinexplorer.name": "Dolphin Explorer",
    "tour.dolphinexplorer.badge": "RECOMENDADO",
    "tour.dolphinexplorer.location": "Punta Cana",
    "tour.dolphinexplorer.note": "",
    "tour.dolphinexplorer.f1": "Transporte de ida e volta",
    "tour.dolphinexplorer.f2": "VISITAR pássaros exóticos",
    "tour.dolphinexplorer.f3": "INTERAÇÃO com Leão Marinho",
    "tour.dolphinexplorer.f4": "INTERAÇÃO com golfinhos (1 hora)",
    "tour.dolphinexplorer.f5": "Armários para guardar seus pertences",
    "tour.dolphinexplorer.f6": "Equipamentos e guias de segurança",
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
            id="cocobongovip"
            img="img/2.jpg" 
            badgeKey="tour.cocobongovip.badge"
            nameKey="tour.cocobongovip.name"
            locationKey="tour.cocobongovip.location"
            noteKey="tour.cocobongovip.note"
            featuresKeys={[
              'tour.cocobongovip.f1', 
              'tour.cocobongovip.f2', 
              'tour.cocobongovip.f3', 
              'tour.cocobongovip.f4',
              'tour.cocobongovip.f5'
            ]}
            delay="d2"
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="cocobongovip"
            img="img/2.jpg" 
            badgeKey="tour.cocobongovip.badge"
            nameKey="tour.cocobongovip.name"
            locationKey="tour.cocobongovip.location"
            noteKey="tour.cocobongovip.note"
            featuresKeys={[
              'tour.cocobongovip.f1', 
              'tour.cocobongovip.f2', 
              'tour.cocobongovip.f3', 
              'tour.cocobongovip.f4',
              'tour.cocobongovip.f5'
            ]}
            delay="d2"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Dolphin Explorer tour")
