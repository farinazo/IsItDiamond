import json

scratch_matched = r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch\matched_animals.json'
with open(scratch_matched, 'r', encoding='utf-8') as f:
    matched = json.load(f)

with open('animals_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

# Master corrections dict: name_en -> {fields to update}
corrections = {
    # 1. Diamond score corrections
    'Spectacled Bear': {'diamond_min': 20.45},
    'Mountain Goat': {'diamond_min': 83.20},
    'Stubble Quail': {'diamond_min': 126.0},
    'Magpie Goose': {'diamond_min': 3.02},
    'Eurasian Woodcock': {'diamond_min': 41.03},
    'Bighorn Sheep': {'diamond_min': 196.93, 'class': 5},
    'Sambar Deer': {'diamond_min': 166.24, 'class': 7},
    'Roe Deer': {'diamond_min': 81.86},

    # 2. Level corrections
    'Ocelot': {'max_level': '9', 'class': 2},
    'Jaguar': {'max_level': '9 (10 Fabled)', 'class': 6},

    # 3. Weapon Class rebalance updates
    'American Alligator': {'class': 7},
    'Saltwater Crocodile': {'class': 8},
    'Grizzly Bear': {'class': 8},
    'Grey Wolf': {'class': 6},
    'Iberian Wolf': {'class': 6},
    'Wild Boar': {'class': 5},
    'Wild Hog': {'class': 5},
    'Feral Pig': {'class': 5},
    'Chamois': {'class': 3},
    'Bobcat': {'class': 2},
    'Mexican Bobcat': {'class': 2},
    'Gemsbok': {'class': 6},
    'Mule Deer': {'class': 5},
    'Puma': {'class': 5},
    'Rocky Mountain Elk': {'class': 7},
    'Javen Rusa': {'class': 5}
}

def apply_corrections(animal_list):
    updated_count = 0
    for a in animal_list:
        name = a.get('name_en')
        if name in corrections:
            corr = corrections[name]
            for k, v in corr.items():
                if a.get(k) != v:
                    print(f"[{name}] {k}: {a.get(k)} -> {v}")
                    a[k] = v
                    updated_count += 1
    return updated_count

print("Applying corrections to matched_animals.json:")
apply_corrections(matched)
with open(scratch_matched, 'w', encoding='utf-8') as f:
    json.dump(matched, f, indent=2, ensure_ascii=False)

print("\nApplying corrections to animals_master.json:")
apply_corrections(master)
with open('animals_master.json', 'w', encoding='utf-8') as f:
    json.dump(master, f, indent=2, ensure_ascii=False)

print("\nApplying corrections to COTW_Overlay_HUD/database.json:")
with open('COTW_Overlay_HUD/database.json', 'w', encoding='utf-8') as f:
    json.dump(matched, f, indent=2, ensure_ascii=False)

print("\nAll database files updated successfully!")
