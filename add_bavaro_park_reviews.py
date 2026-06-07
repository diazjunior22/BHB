import json

files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.bavaropark.notIncluded1": "Propinas",
    "tour.bavaropark.notIncluded2": "Bebidas durante el almuerzo",
    "tour.bavaropark.notIncluded3": "Fotografías o souvenirs",
    "tour.bavaropark.review1Name": "Juan P.",
    "tour.bavaropark.review1Text": "¡Increíble experiencia! Combinar dos actividades extremas fue lo mejor de nuestras vacaciones.",
    "tour.bavaropark.review2Name": "Marta G.",
    "tour.bavaropark.review2Text": "Excelente organización y los guías muy amables. El Zip Line es una pasada.",
    "tour.bavaropark.rating": "4.9",
    "tour.bavaropark.reviewsCount": "342"
}

data_en = {
    "tour.bavaropark.notIncluded1": "Tips",
    "tour.bavaropark.notIncluded2": "Drinks during lunch",
    "tour.bavaropark.notIncluded3": "Photos or souvenirs",
    "tour.bavaropark.review1Name": "John P.",
    "tour.bavaropark.review1Text": "Incredible experience! Combining two extreme activities was the highlight of our vacation.",
    "tour.bavaropark.review2Name": "Martha G.",
    "tour.bavaropark.review2Text": "Excellent organization and very friendly guides. The Zip Line is amazing.",
    "tour.bavaropark.rating": "4.9",
    "tour.bavaropark.reviewsCount": "342"
}

data_pt = {
    "tour.bavaropark.notIncluded1": "Gorjetas",
    "tour.bavaropark.notIncluded2": "Bebidas durante o almoço",
    "tour.bavaropark.notIncluded3": "Fotos ou lembranças",
    "tour.bavaropark.review1Name": "João P.",
    "tour.bavaropark.review1Text": "Experiência incrível! Combinar duas atividades extremas foi o ponto alto das nossas férias.",
    "tour.bavaropark.review2Name": "Marta G.",
    "tour.bavaropark.review2Text": "Excelente organização e guias muito simpáticos. A Tirolesa é fantástica.",
    "tour.bavaropark.rating": "4.9",
    "tour.bavaropark.reviewsCount": "342"
}

updates = {'es': data_es, 'en': data_en, 'pt': data_pt}

for lang, filepath in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    content.update(updates[lang])
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

print("Added Bavaro Adventure Park reviews and ratings")
