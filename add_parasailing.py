import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.parasailing.name": "Parasailing",
    "tour.parasailing.badge": "RECOMENDADO",
    "tour.parasailing.location": "Punta Cana",
    "tour.parasailing.note": "Los hoteles del área de Cap Cana y Uvero Alto deben pagar una tarifa adicional de transporte.",
    "tour.parasailing.f1": "Transporte ida y vuelta",
    "tour.parasailing.f2": "30 minutos en el aire",
    "tour.parasailing.f3": "Guías profesionales",
    "tour.parasailing.f4": "Equipos de seguridad",
    "tour.parasailing.f5": "Tiempo en playa bávaro",
}

data_en = {
    "tour.parasailing.name": "Parasailing",
    "tour.parasailing.badge": "RECOMMENDED",
    "tour.parasailing.location": "Punta Cana",
    "tour.parasailing.note": "Hotels in the Cap Cana and Uvero Alto area must pay an additional transportation fee.",
    "tour.parasailing.f1": "Round trip transportation",
    "tour.parasailing.f2": "30 minutes in the air",
    "tour.parasailing.f3": "Professional guides",
    "tour.parasailing.f4": "Security equipments",
    "tour.parasailing.f5": "Bavaro beach weather",
}

data_pt = {
    "tour.parasailing.name": "Parasailing",
    "tour.parasailing.badge": "RECOMENDADO",
    "tour.parasailing.location": "Punta Cana",
    "tour.parasailing.note": "Hotéis na área de Cap Cana e Uvero Alto devem pagar uma taxa de transporte adicional.",
    "tour.parasailing.f1": "Transporte de ida e volta",
    "tour.parasailing.f2": "30 minutos no ar",
    "tour.parasailing.f3": "Guias profissionais",
    "tour.parasailing.f4": "Equipamentos de segurança",
    "tour.parasailing.f5": "Clima na praia de Bávaro",
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
          />

          <TourCard 
            id="parasailing"
            img="img/catamaran.png" 
            badgeKey="tour.parasailing.badge"
            nameKey="tour.parasailing.name"
            locationKey="tour.parasailing.location"
            noteKey="tour.parasailing.note"
            featuresKeys={[
              'tour.parasailing.f1', 
              'tour.parasailing.f2', 
              'tour.parasailing.f3', 
              'tour.parasailing.f4',
              'tour.parasailing.f5'
            ]}
            delay="d2"
          />"""

grid_content = grid_content.replace("""          <TourCard 
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
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Parasailing tour")
