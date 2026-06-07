import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.pescafishing.name": "Pesca Fishing",
    "tour.pescafishing.badge": "RECOMENDADO",
    "tour.pescafishing.location": "Punta Cana",
    "tour.pescafishing.note": "SE DEBE PAGAR CON ANTICIPACIÓN PARA LA RESERVACIÓN DEL BARCO",
    "tour.pescafishing.f1": "Transporte privado de ida y vuelta",
    "tour.pescafishing.f2": "Capitán y 1er. Compañero",
    "tour.pescafishing.f3": "Abordajes resistentes",
    "tour.pescafishing.f4": "Cebos para la pesca",
    "tour.pescafishing.f5": "Combustible",
    "tour.pescafishing.f6": "Gaseosas y Agua",
    "tour.pescafishing.f7": "Todos los impuestos, licencia, tasas y gastos de tramitación",
}

data_en = {
    "tour.pescafishing.name": "Pesca Fishing",
    "tour.pescafishing.badge": "RECOMMENDED",
    "tour.pescafishing.location": "Punta Cana",
    "tour.pescafishing.note": "YOU MUST PAY IN ADVANCE FOR BOAT RESERVATION",
    "tour.pescafishing.f1": "Round-trip private transportation",
    "tour.pescafishing.f2": "Captain and 1st Buddy",
    "tour.pescafishing.f3": "Resistant approaches",
    "tour.pescafishing.f4": "Baits for fishing",
    "tour.pescafishing.f5": "Fuel",
    "tour.pescafishing.f6": "Sodas and Water",
    "tour.pescafishing.f7": "All taxes, license, fees and processing fees",
}

data_pt = {
    "tour.pescafishing.name": "Pesca Fishing",
    "tour.pescafishing.badge": "RECOMENDADO",
    "tour.pescafishing.location": "Punta Cana",
    "tour.pescafishing.note": "VOCÊ DEVE PAGAR ANTECIPADO PELA RESERVA DO BARCO",
    "tour.pescafishing.f1": "Transporte privado de ida e volta",
    "tour.pescafishing.f2": "Capitão e 1º. Companheiro",
    "tour.pescafishing.f3": "Abordagens resistentes",
    "tour.pescafishing.f4": "Iscas para pesca",
    "tour.pescafishing.f5": "Combustível",
    "tour.pescafishing.f6": "Refrigerantes e Água",
    "tour.pescafishing.f7": "Todos os impostos, licenças, taxas e taxas de processamento",
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
          />

          <TourCard 
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
          />"""

grid_content = grid_content.replace("""          <TourCard 
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
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added Pesca Fishing tour")
