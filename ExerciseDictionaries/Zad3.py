from collections import defaultdict

key_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_item = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk = defaultdict(int)
winner = ""
while winner == "":
    text = input().lower().split(" ")
    for i in range(0, len(text), 2):
        material = text[i + 1]
        quantity = text[i]
        if material in key_materials:
            key_materials[material] += int(quantity)
            if key_materials[material] >= 250:
                winner = material
                break
        else:
            junk[material] += int(quantity)

key_materials[material] -= 250
print(f"{legendary_item[winner]} obtained!")

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items()))
key_materials.update(junk)
for key, value in key_materials.items():
    print(f"{key}: {value}")
# for key, value in junk.items():
#     print(f"{key}: {value}")
