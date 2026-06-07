import json
import os

files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

data_es = {
    "tour.saonavip.badge": "VIP",
    "tour.saonavip.name": "Isla Saona VIP 3 Playa",
    "tour.saonavip.location": "Isla Saona · Parque Nacional del Este",
    "tour.saonavip.note": "Niños hasta 11 años tienen precio especial.",
    "tour.saonavip.f1": "Transporte terrestre y marítimo (Lancha Rápida/Catamarán)",
    "tour.saonavip.f2": "Visita a 3 playas exclusivas",
    "tour.saonavip.f3": "Almuerzo buffet premium + bebidas",
    "tour.saonavip.f4": "Guía oficial y animación VIP",
    "tour.saonavip.duration": "8 horas",
    "tour.saonavip.price": "120",
    "tour.saonavip.shortDesc": "Disfruta de una experiencia VIP inolvidable con visita a 3 playas exclusivas.",
    "tour.saonavip.importantInfo": "Llevar protector solar, ropa cómoda, traje de baño y toalla. No apto para mujeres embarazadas.",
    "tour.saonavip.iti1": "08:00 AM - Recogida en el hotel",
    "tour.saonavip.iti2": "09:30 AM - Llegada al destino",
    "tour.saonavip.iti3": "12:30 PM - Almuerzo buffet",
    "tour.saonavip.iti4": "03:00 PM - Tiempo libre en la playa",
    "tour.saonavip.iti5": "05:00 PM - Retorno al hotel",
    "tour.saonavip.notIncluded1": "Gastos personales y souvenirs",
    "tour.saonavip.notIncluded2": "Propinas (opcional)",
    "tour.saonavip.notIncluded3": "Fotos profesionales",
    "tour.saonavip.rating": "5.0",
    "tour.saonavip.reviewsCount": "145"
}

data_en = {
    "tour.saonavip.badge": "VIP",
    "tour.saonavip.name": "Isla Saona VIP 3 Playa",
    "tour.saonavip.location": "Saona Island · East National Park",
    "tour.saonavip.note": "Children up to 11 years old have a special price.",
    "tour.saonavip.f1": "Land and sea transportation (Speedboat/Catamaran)",
    "tour.saonavip.f2": "Visit to 3 exclusive beaches",
    "tour.saonavip.f3": "Premium buffet lunch + drinks",
    "tour.saonavip.f4": "Official guide and VIP entertainment",
    "tour.saonavip.duration": "8 hours",
    "tour.saonavip.price": "120",
    "tour.saonavip.shortDesc": "Enjoy an unforgettable VIP experience with a visit to 3 exclusive beaches.",
    "tour.saonavip.importantInfo": "Bring sunscreen, comfortable clothes, swimsuit and towel. Not suitable for pregnant women.",
    "tour.saonavip.iti1": "08:00 AM - Hotel pickup",
    "tour.saonavip.iti2": "09:30 AM - Arrival at destination",
    "tour.saonavip.iti3": "12:30 PM - Buffet lunch",
    "tour.saonavip.iti4": "03:00 PM - Free time at the beach",
    "tour.saonavip.iti5": "05:00 PM - Return to hotel",
    "tour.saonavip.notIncluded1": "Personal expenses and souvenirs",
    "tour.saonavip.notIncluded2": "Tips (optional)",
    "tour.saonavip.notIncluded3": "Professional photos",
    "tour.saonavip.rating": "5.0",
    "tour.saonavip.reviewsCount": "145"
}

data_pt = {
    "tour.saonavip.badge": "VIP",
    "tour.saonavip.name": "Isla Saona VIP 3 Playa",
    "tour.saonavip.location": "Ilha Saona · Parque Nacional do Leste",
    "tour.saonavip.note": "Crianças até 11 anos têm preço especial.",
    "tour.saonavip.f1": "Transporte terrestre e marítimo (Lancha/Catamarã)",
    "tour.saonavip.f2": "Visita a 3 praias exclusivas",
    "tour.saonavip.f3": "Almoço buffet premium + bebidas",
    "tour.saonavip.f4": "Guia oficial e animação VIP",
    "tour.saonavip.duration": "8 horas",
    "tour.saonavip.price": "120",
    "tour.saonavip.shortDesc": "Desfrute de uma experiência VIP inesquecível com visita a 3 praias exclusivas.",
    "tour.saonavip.importantInfo": "Leve protetor solar, roupas confortáveis, roupa de banho e toalha. Não recomendado para mulheres grávidas.",
    "tour.saonavip.iti1": "08:00 AM - Traslado do hotel",
    "tour.saonavip.iti2": "09:30 AM - Chegada ao destino",
    "tour.saonavip.iti3": "12:30 PM - Almoço buffet",
    "tour.saonavip.iti4": "03:00 PM - Tempo livre na praia",
    "tour.saonavip.iti5": "05:00 PM - Retorno ao hotel",
    "tour.saonavip.notIncluded1": "Despesas pessoais e souvenirs",
    "tour.saonavip.notIncluded2": "Gorjetas (opcional)",
    "tour.saonavip.notIncluded3": "Fotos profissionais",
    "tour.saonavip.rating": "5.0",
    "tour.saonavip.reviewsCount": "145"
}

updates = {'es': data_es, 'en': data_en, 'pt': data_pt}

for lang, filepath in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    content.update(updates[lang])
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

print("Added Saona VIP to locales")
