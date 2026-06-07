import json
import os
import re

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.bavaropark.name": "Bávaro Adventure Park (2 Actividades)",
    "tour.bavaropark.badge": "RECOMENDADO",
    "tour.bavaropark.location": "Punta Cana",
    "tour.bavaropark.note": "Escoge 2 actividades de las disponibles",
    "tour.bavaropark.f1": "Transporte ida y vuelta",
    "tour.bavaropark.f2": "Tour de Buggy o Polaris",
    "tour.bavaropark.f3": "Zip Line",
    "tour.bavaropark.f4": "Paseo a Caballo",
    "tour.bavaropark.f5": "Splash of Emotions (Jungle River, Cenote Blue Lagoon, Piscina)",
    "tour.bavaropark.duration": "8 horas",
    "tour.bavaropark.price": "139",
    "tour.bavaropark.shortDesc": "Combina 2 actividades extremas y disfruta de un día lleno de adrenalina.",
    "tour.bavaropark.importantInfo": "Llevar protector solar, ropa cómoda, traje de baño y toalla.",
    "tour.bavaropark.iti1": "08:00 AM - Recogida en el hotel",
    "tour.bavaropark.iti2": "09:30 AM - Llegada al parque y briefing",
    "tour.bavaropark.iti3": "10:00 AM - Inicio de actividades",
    "tour.bavaropark.iti4": "01:00 PM - Almuerzo (no incluye bebidas)",
    "tour.bavaropark.iti5": "04:00 PM - Retorno al hotel"
}

data_en = {
    "tour.bavaropark.name": "Bávaro Adventure Park (2 Activities)",
    "tour.bavaropark.badge": "RECOMMENDED",
    "tour.bavaropark.location": "Punta Cana",
    "tour.bavaropark.note": "Choose 2 of the available activities",
    "tour.bavaropark.f1": "Round trip transportation",
    "tour.bavaropark.f2": "Buggy or Polaris Tour",
    "tour.bavaropark.f3": "Zip Line",
    "tour.bavaropark.f4": "Horseback Riding",
    "tour.bavaropark.f5": "Splash of Emotions (Jungle River, Cenote Blue Lagoon, Pool)",
    "tour.bavaropark.duration": "8 hours",
    "tour.bavaropark.price": "139",
    "tour.bavaropark.shortDesc": "Combine 2 extreme activities and enjoy an adrenaline-filled day.",
    "tour.bavaropark.importantInfo": "Bring sunscreen, comfortable clothes, swimsuit and towel.",
    "tour.bavaropark.iti1": "08:00 AM - Hotel pickup",
    "tour.bavaropark.iti2": "09:30 AM - Arrival at the park and briefing",
    "tour.bavaropark.iti3": "10:00 AM - Start of activities",
    "tour.bavaropark.iti4": "01:00 PM - Lunch (drinks not included)",
    "tour.bavaropark.iti5": "04:00 PM - Return to hotel"
}

data_pt = {
    "tour.bavaropark.name": "Bávaro Adventure Park (2 Atividades)",
    "tour.bavaropark.badge": "RECOMENDADO",
    "tour.bavaropark.location": "Punta Cana",
    "tour.bavaropark.note": "Escolha 2 das atividades disponíveis",
    "tour.bavaropark.f1": "Transporte de ida e volta",
    "tour.bavaropark.f2": "Tour de Buggy ou Polaris",
    "tour.bavaropark.f3": "Tirolesa (Zip Line)",
    "tour.bavaropark.f4": "Passeio a Cavalo",
    "tour.bavaropark.f5": "Splash of Emotions (Jungle River, Cenote Blue Lagoon, Piscina)",
    "tour.bavaropark.duration": "8 horas",
    "tour.bavaropark.price": "139",
    "tour.bavaropark.shortDesc": "Combine 2 atividades extremas e desfrute de um dia repleto de adrenalina.",
    "tour.bavaropark.importantInfo": "Traga protetor solar, roupas confortáveis, roupa de banho e toalha.",
    "tour.bavaropark.iti1": "08:00 AM - Recolha no hotel",
    "tour.bavaropark.iti2": "09:30 AM - Chegada ao parque e briefing",
    "tour.bavaropark.iti3": "10:00 AM - Início das atividades",
    "tour.bavaropark.iti4": "01:00 PM - Almoço (bebidas não incluídas)",
    "tour.bavaropark.iti5": "04:00 PM - Retorno ao hotel"
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
            id="bavaropark"
            img={imgAtv} 
            badgeKey="tour.bavaropark.badge"
            nameKey="tour.bavaropark.name"
            locationKey="tour.bavaropark.location"
            noteKey="tour.bavaropark.note"
            featuresKeys={[
              'tour.bavaropark.f1', 
              'tour.bavaropark.f2', 
              'tour.bavaropark.f3', 
              'tour.bavaropark.f4',
              'tour.bavaropark.f5'
            ]}
            delay="d1"
          />
        </div>
      </div>
    </section>"""

grid_content = grid_content.replace("""        </div>\n      </div>\n    </section>""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

# Update TourDetail.jsx
detail_file = 'src/pages/TourDetail.jsx'
with open(detail_file, 'r', encoding='utf-8') as f:
    detail_content = f.read()

detail_content = detail_content.replace(
    "  default: { hero:",
    "  bavaropark: { hero: heroAtv, gallery: getGallery([boguie1, boguie2, boguie3, boguie4, boguie5]) },\n  default: { hero:"
)

with open(detail_file, 'w', encoding='utf-8') as f:
    f.write(detail_content)

print("Added Bavaro Adventure Park tour")
