import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.haciendapark.name": "Hacienda Park",
    "tour.haciendapark.badge": "RECOMENDADO",
    "tour.haciendapark.location": "Punta Cana",
    "tour.haciendapark.note": "Niños hasta 11 años tienen precio especial",
    "tour.haciendapark.f1": "Transporte ida y vuelta",
    "tour.haciendapark.f2": "Booguie doble o familiar",
    "tour.haciendapark.f3": "Paseo a Caballo",
    "tour.haciendapark.f4": "Safari en campos dominicanos",
    "tour.haciendapark.f5": "ZipLine en medio de las montañas",
    "tour.haciendapark.f6": "Caída libre de 20 mtrs",
    "tour.haciendapark.f7": "Telesilla",
    "tour.haciendapark.f8": "Almuerzo típico y bebidas",
    "tour.haciendapark.f9": "Equipos de seguridad",
    "tour.haciendapark.f10": "Guías expertos",
}

data_en = {
    "tour.haciendapark.name": "Hacienda Park",
    "tour.haciendapark.badge": "RECOMMENDED",
    "tour.haciendapark.location": "Punta Cana",
    "tour.haciendapark.note": "Children under the age of 11 have a special price",
    "tour.haciendapark.f1": "Round trip transportation",
    "tour.haciendapark.f2": "Double or family booguie",
    "tour.haciendapark.f3": "Horse ride",
    "tour.haciendapark.f4": "Safari in Dominican fields",
    "tour.haciendapark.f5": "ZipLine in the middle of the mountains",
    "tour.haciendapark.f6": "Free fall of 20 meters",
    "tour.haciendapark.f7": "Chairlift",
    "tour.haciendapark.f8": "Typical lunch and drinks",
    "tour.haciendapark.f9": "Security equipments",
    "tour.haciendapark.f10": "Expert guides",
}

data_pt = {
    "tour.haciendapark.name": "Hacienda Park",
    "tour.haciendapark.badge": "RECOMENDADO",
    "tour.haciendapark.location": "Punta Cana",
    "tour.haciendapark.note": "Crianças até aos 11 anos têm um preço especial",
    "tour.haciendapark.f1": "Transporte de ida e volta",
    "tour.haciendapark.f2": "Booguie duplo ou familiar",
    "tour.haciendapark.f3": "Passeio a cavalo",
    "tour.haciendapark.f4": "Safari nos campos dominicanos",
    "tour.haciendapark.f5": "Tirolesa no meio das montanhas",
    "tour.haciendapark.f6": "Queda livre de 20 metros",
    "tour.haciendapark.f7": "Teleférico",
    "tour.haciendapark.f8": "Almoço típico e bebidas",
    "tour.haciendapark.f9": "Equipamentos de segurança",
    "tour.haciendapark.f10": "Guias especializados",
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
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
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
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Hacienda Park tour")
