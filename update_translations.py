import json
import os

files = {
    'es': 'src/locales/es.json',
    'en': 'src/locales/en.json',
    'pt': 'src/locales/pt.json'
}

tours = [
    "saona", "party", "atv", "polarys", "santodomingo", "cocobongo", 
    "cocobongovip", "dolphinexplorer", "scapepark", "haciendapark", 
    "scubadoo", "pescafishing", "funpark", "samana", "catalinaisland", 
    "parasailing", "eldorado"
]

def get_placeholders(lang):
    if lang == 'es':
        return {
            "notIncluded1": "Gastos personales y souvenirs",
            "notIncluded2": "Propinas (opcional)",
            "notIncluded3": "Fotos profesionales",
            "review1Name": "Carlos M.",
            "review1Text": "¡La mejor experiencia de nuestro viaje! Todo estuvo perfectamente organizado y el guía fue increíble.",
            "review2Name": "Laura G.",
            "review2Text": "Totalmente recomendado. Una aventura inolvidable, sin duda volveremos a reservar con ustedes.",
            "rating": "4.9",
            "reviewsCount": "327"
        }
    elif lang == 'en':
        return {
            "notIncluded1": "Personal expenses and souvenirs",
            "notIncluded2": "Tips (optional)",
            "notIncluded3": "Professional photos",
            "review1Name": "Charles M.",
            "review1Text": "The best experience of our trip! Everything was perfectly organized and the guide was amazing.",
            "review2Name": "Laura G.",
            "review2Text": "Totally recommended. An unforgettable adventure, we will definitely book with you again.",
            "rating": "4.9",
            "reviewsCount": "327"
        }
    else: # pt
        return {
            "notIncluded1": "Despesas pessoais e lembranças",
            "notIncluded2": "Gorjetas (opcional)",
            "notIncluded3": "Fotos profissionais",
            "review1Name": "Carlos M.",
            "review1Text": "A melhor experiência da nossa viagem! Tudo foi perfeitamente organizado e o guia foi incrível.",
            "review2Name": "Laura G.",
            "review2Text": "Totalmente recomendado. Uma aventura inesquecível, com certeza reservaremos com vocês novamente.",
            "rating": "4.9",
            "reviewsCount": "327"
        }

for lang, filepath in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = json.load(f)
    
    placeholders = get_placeholders(lang)
    
    for t_id in tours:
        for key, val in placeholders.items():
            if f"tour.{t_id}.{key}" not in content:
                content[f"tour.{t_id}.{key}"] = val

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

print("Translations updated successfully.")
