import json
import os

# Update translations
files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.eldorado.name": "El Dorado Park",
    "tour.eldorado.badge": "",
    "tour.eldorado.location": "Punta Cana",
    "tour.eldorado.note": "Horario: Jueves a Domingo (10:00am - 5:00pm)",
    "tour.eldorado.f1": "Servicio de transporte incluido (Revisar condiciones)",
    "tour.eldorado.f2": "Acceso a todas las atracciones y áreas de descanso",
    "tour.eldorado.f3": "Equipos para las actividades",
    "tour.eldorado.f4": "Uso libre de hamacas y sombrillas",
    "tour.eldorado.f5": "No incluye alimentos y bebidas",
    "tour.eldorado.f6": "Adultos (+13 años): $129 USD",
    "tour.eldorado.f7": "Niños (4-12 años): $69 USD",
    "tour.eldorado.f8": "Infantes (0-3 años): GRATIS",
}

data_en = {
    "tour.eldorado.name": "El Dorado Park",
    "tour.eldorado.badge": "",
    "tour.eldorado.location": "Punta Cana",
    "tour.eldorado.note": "Schedule: Thursday to Sunday (10:00am - 5:00pm)",
    "tour.eldorado.f1": "Transportation service included (Check conditions)",
    "tour.eldorado.f2": "Access to all attractions and rest areas",
    "tour.eldorado.f3": "Equipment for activities",
    "tour.eldorado.f4": "Free use of hammocks and umbrellas",
    "tour.eldorado.f5": "Food and drinks not included",
    "tour.eldorado.f6": "Adults (13+ years): $129 USD",
    "tour.eldorado.f7": "Kids (4-12 years): $69 USD",
    "tour.eldorado.f8": "Toddlers (0-3 years): FREE",
}

data_pt = {
    "tour.eldorado.name": "El Dorado Park",
    "tour.eldorado.badge": "",
    "tour.eldorado.location": "Punta Cana",
    "tour.eldorado.note": "Horário: Quinta a Domingo (10:00am - 5:00pm)",
    "tour.eldorado.f1": "Serviço de transporte incluído (Verificar condições)",
    "tour.eldorado.f2": "Acesso a todas as atrações e áreas de descanso",
    "tour.eldorado.f3": "Equipamentos para atividades",
    "tour.eldorado.f4": "Uso livre de redes e guarda-sóis",
    "tour.eldorado.f5": "Alimentos e bebidas não incluídos",
    "tour.eldorado.f6": "Adultos (+13 anos): $129 USD",
    "tour.eldorado.f7": "Crianças (4-12 anos): $69 USD",
    "tour.eldorado.f8": "Bebês (0-3 anos): GRÁTIS",
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
          />

          <TourCard 
            id="eldorado"
            img="img/1.jpg" 
            badgeKey="tour.eldorado.badge"
            nameKey="tour.eldorado.name"
            locationKey="tour.eldorado.location"
            noteKey="tour.eldorado.note"
            featuresKeys={[
              'tour.eldorado.f1', 
              'tour.eldorado.f2', 
              'tour.eldorado.f3', 
              'tour.eldorado.f4',
              'tour.eldorado.f5',
              'tour.eldorado.f6',
              'tour.eldorado.f7',
              'tour.eldorado.f8'
            ]}
            delay="d3"
          />"""

grid_content = grid_content.replace("""          <TourCard 
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
          />""", new_card)

with open(grid_file, 'w', encoding='utf-8') as f:
    f.write(grid_content)

print("Added El Dorado Park tour")
