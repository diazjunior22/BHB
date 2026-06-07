import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.cocobongovip.name": "Coco Bongo VIP",
    "tour.cocobongovip.badge": "RECOMENDADO",
    "tour.cocobongovip.location": "Punta Cana",
    "tour.cocobongovip.note": "Transporte PRIVADO 20 dólares adicionales",
    "tour.cocobongovip.f1": "Transporte Ida y Vuelta",
    "tour.cocobongovip.f2": "Barra Libre Toda la Noche (Bebidas Premium)",
    "tour.cocobongovip.f3": "Snacks y Entrada Preferencial sin Filas",
    "tour.cocobongovip.f4": "FRONT ROW: Mesas preferenciales y camareros personales",
    "tour.cocobongovip.f5": "GOLD MEMBER: Mesas en segundo piso con camareros",
}

data_en = {
    "tour.cocobongovip.name": "Coco Bongo VIP",
    "tour.cocobongovip.badge": "RECOMMENDED",
    "tour.cocobongovip.location": "Punta Cana",
    "tour.cocobongovip.note": "PRIVATE transportation 20 additional dollars",
    "tour.cocobongovip.f1": "Round Transportation",
    "tour.cocobongovip.f2": "Open Bar All Night (Premium Drinks)",
    "tour.cocobongovip.f3": "Snacks and Preferential Entry without lines",
    "tour.cocobongovip.f4": "FRONT ROW: Preferential tables and personal waitress",
    "tour.cocobongovip.f5": "GOLD MEMBER: Tables on the second floor with waiters",
}

data_pt = {
    "tour.cocobongovip.name": "Coco Bongo VIP",
    "tour.cocobongovip.badge": "RECOMENDADO",
    "tour.cocobongovip.location": "Punta Cana",
    "tour.cocobongovip.note": "Transporte PRIVADO 20 dólares adicionais",
    "tour.cocobongovip.f1": "Transporte Ida e Volta",
    "tour.cocobongovip.f2": "Open Bar Toda a Noite (Premium Drinks)",
    "tour.cocobongovip.f3": "Lanches e Entrada Preferencial sem Filas",
    "tour.cocobongovip.f4": "FRONT ROW: Mesas preferenciais e garçonete personal",
    "tour.cocobongovip.f5": "GOLD MEMBER: Mesas no segundo andar com garçons",
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
            id="cocobongo"
            img="img/1.jpg" 
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
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
            id="cocobongo"
            img="img/1.jpg" 
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
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Coco Bongo VIP tour")
