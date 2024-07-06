import json
with open("facult.json", 'r', encoding='utf-8-sig') as file:
    a = file.read().replace(';', ' ')

with open("facult2.json", "w") as file:
    json.dump(a, file, indent=4, ensure_ascii=False)