import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.scubadoo.name": "Scuba Doo",
    "tour.scubadoo.badge": "RECOMENDADO",
    "tour.scubadoo.location": "Punta Cana",
    "tour.scubadoo.note": "",
    "tour.scubadoo.f1": "Transporte ida y vuelta",
    "tour.scubadoo.f2": "Bebidas no alcohólicas",
    "tour.scubadoo.f3": "Snorkel de 1 hora",
    "tour.scubadoo.f4": "Inmersión de 1 hora",
    "tour.scubadoo.f5": "Snacks ligeros",
    "tour.scubadoo.f6": "Equipos de seguridad",
    "tour.scubadoo.f7": "Barco con fondo de cristal para disfrutar de todo el viaje",
}

data_en = {
    "tour.scubadoo.name": "Scuba Doo",
    "tour.scubadoo.badge": "RECOMMENDED",
    "tour.scubadoo.location": "Punta Cana",
    "tour.scubadoo.note": "",
    "tour.scubadoo.f1": "Round trip transportation",
    "tour.scubadoo.f2": "Non-alcoholic beverages",
    "tour.scubadoo.f3": "1 hour snorkeling",
    "tour.scubadoo.f4": "1 hour dive",
    "tour.scubadoo.f5": "Light snacks",
    "tour.scubadoo.f6": "Security equipments",
    "tour.scubadoo.f7": "Glass bottom boat to enjoy the whole trip",
}

data_pt = {
    "tour.scubadoo.name": "Scuba Doo",
    "tour.scubadoo.badge": "RECOMENDADO",
    "tour.scubadoo.location": "Punta Cana",
    "tour.scubadoo.note": "",
    "tour.scubadoo.f1": "Transporte de ida e volta",
    "tour.scubadoo.f2": "Bebidas não alcoólicas",
    "tour.scubadoo.f3": "1 hora de snorkel",
    "tour.scubadoo.f4": "1 hora de mergulho",
    "tour.scubadoo.f5": "Aperitivos leves",
    "tour.scubadoo.f6": "Equipamentos de segurança",
    "tour.scubadoo.f7": "Barco com fundo de vidro para aproveitar toda a viagem",
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
            id="haciendapark"
            img="img/2.jpg" 
            badgeKey="tour.haciendapark.badge"
            nameKey="tour.haciendapark.name"
            locationKey="tour.haciendapark.location"
            noteKey="tour.haciendapark.note"
            featuresKeys={[
              'tour.haciendapark.f1', 
              'tour.haciendapark.f2', 
              'tour.haciendapark.f3', 
              'tour.haciendapark.f4',
              'tour.haciendapark.f5',
              'tour.haciendapark.f6',
              'tour.haciendapark.f7',
              'tour.haciendapark.f8',
              'tour.haciendapark.f9',
              'tour.haciendapark.f10'
            ]}
            delay="d2"
          />

          <TourCard 
            id="scubadoo"
            img="img/1.jpg" 
            badgeKey="tour.scubadoo.badge"
            nameKey="tour.scubadoo.name"
            locationKey="tour.scubadoo.location"
            noteKey="tour.scubadoo.note"
            featuresKeys={[
              'tour.scubadoo.f1', 
              'tour.scubadoo.f2', 
              'tour.scubadoo.f3', 
              'tour.scubadoo.f4',
              'tour.scubadoo.f5',
              'tour.scubadoo.f6',
              'tour.scubadoo.f7'
            ]}
            delay="d3"
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="haciendapark"
            img="img/2.jpg" 
            badgeKey="tour.haciendapark.badge"
            nameKey="tour.haciendapark.name"
            locationKey="tour.haciendapark.location"
            noteKey="tour.haciendapark.note"
            featuresKeys={[
              'tour.haciendapark.f1', 
              'tour.haciendapark.f2', 
              'tour.haciendapark.f3', 
              'tour.haciendapark.f4',
              'tour.haciendapark.f5',
              'tour.haciendapark.f6',
              'tour.haciendapark.f7',
              'tour.haciendapark.f8',
              'tour.haciendapark.f9',
              'tour.haciendapark.f10'
            ]}
            delay="d2"
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Scuba Doo tour")
