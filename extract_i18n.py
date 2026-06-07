import re
import json

with open('src/legacy.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract dictionaries
es_match = re.search(r"es:\s*({.*?})", content, re.DOTALL)
en_match = re.search(r"en:\s*({.*?})", content, re.DOTALL)
pt_match = re.search(r"pt:\s*({.*?})", content, re.DOTALL)

def clean_dict_str(s):
    # Convert JS object string to JSON
    # It might have unquoted keys, single quotes, etc.
    # It's safer to just use a regex to extract keys and values
    matches = re.findall(r"'([^']+)':\s*'([^']*)'", s)
    return {k: v for k, v in matches}

if es_match:
    es_dict = clean_dict_str(es_match.group(1))
    
    # Add Santo Domingo tour manually to dictionaries
    es_dict.update({
        "tour.santodomingo.name": "City Tour in Santo Domingo",
        "tour.santodomingo.badge": "RECOMENDADO",
        "tour.santodomingo.location": "Santo Domingo",
        "tour.santodomingo.note": "Nota: Niños hasta 11 años tienen precio especial",
        "tour.santodomingo.f1": "Cueva de los tres ojos",
        "tour.santodomingo.f2": "Museo Faro a Colón",
        "tour.santodomingo.f3": "Palacio Presidencial",
        "tour.santodomingo.f4": "Zona Colonial",
        "tour.santodomingo.f5": "Calle \"El Conde\"",
        "tour.santodomingo.f6": "Calle \"Las Damas\"",
        "tour.santodomingo.f7": "Fortaleza Osama",
        "tour.santodomingo.f8": "1era Catedral",
        "tour.santodomingo.f9": "Panteón Nacional",
        "tour.santodomingo.f10": "Museo de la Casa Real",
        "tour.santodomingo.f11": "Casa Diego Colón",
        "tour.santodomingo.f12": "Almuerzo y bebidas NO alcohólicas",
    })
    
    import os
    os.makedirs('src/locales', exist_ok=True)
    with open('src/locales/es.json', 'w', encoding='utf-8') as f:
        json.dump(es_dict, f, ensure_ascii=False, indent=2)

if en_match:
    en_dict = clean_dict_str(en_match.group(1))
    en_dict.update({
        "tour.santodomingo.name": "City Tour in Santo Domingo",
        "tour.santodomingo.badge": "RECOMMENDED",
        "tour.santodomingo.location": "Santo Domingo",
        "tour.santodomingo.note": "Note: Children under the age of 11 have a special price",
        "tour.santodomingo.f1": "Cave of the three eyes",
        "tour.santodomingo.f2": "Columbus Lighthouse Museum",
        "tour.santodomingo.f3": "Presidential palace",
        "tour.santodomingo.f4": "Colonial Zone",
        "tour.santodomingo.f5": "Street \"El Conde\"",
        "tour.santodomingo.f6": "Street \"Las Damas\"",
        "tour.santodomingo.f7": "Osama Fortress",
        "tour.santodomingo.f8": "1st Cathedral",
        "tour.santodomingo.f9": "National Panteon",
        "tour.santodomingo.f10": "Museum of the Royal House",
        "tour.santodomingo.f11": "Diego Colon House",
        "tour.santodomingo.f12": "Lunch and non-alcoholic drinks",
    })
    with open('src/locales/en.json', 'w', encoding='utf-8') as f:
        json.dump(en_dict, f, ensure_ascii=False, indent=2)

if pt_match:
    pt_dict = clean_dict_str(pt_match.group(1))
    pt_dict.update({
        "tour.santodomingo.name": "City Tour in Santo Domingo",
        "tour.santodomingo.badge": "RECOMENDADO",
        "tour.santodomingo.location": "Santo Domingo",
        "tour.santodomingo.note": "Nota: Crianças até aos 11 anos têm um preço especial",
        "tour.santodomingo.f1": "Caverna dos três olhos",
        "tour.santodomingo.f2": "Museu do Farol de Colombo",
        "tour.santodomingo.f3": "Palácio presidencial",
        "tour.santodomingo.f4": "Zona Colonial",
        "tour.santodomingo.f5": "Rua \"El Conde\"",
        "tour.santodomingo.f6": "Rua \"Las Damas\"",
        "tour.santodomingo.f7": "Fortaleza de Osama",
        "tour.santodomingo.f8": "1ª Catedral",
        "tour.santodomingo.f9": "Panteão Nacional",
        "tour.santodomingo.f10": "Museu da Casa Real",
        "tour.santodomingo.f11": "Casa Diego Colón",
        "tour.santodomingo.f12": "Almoço e bebidas não alcoólicas",
    })
    with open('src/locales/pt.json', 'w', encoding='utf-8') as f:
        json.dump(pt_dict, f, ensure_ascii=False, indent=2)

print("i18n extracted to JSON files")
