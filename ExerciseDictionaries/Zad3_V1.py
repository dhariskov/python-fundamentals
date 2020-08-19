from collections import defaultdict


def validate_key_existing(dictionary, key, def_value=0):
    if key not in dictionary:
        dictionary[key] = def_value


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

# junk = defaultdict(int)
junk = {}
winner = ""
while winner == "":
    text = input().lower().split(" ")
    for i in range(0, len(text), 2):
        if text[i + 1] in key_materials:
            key_materials[text[i + 1]] += int(text[i])
            if key_materials[text[i + 1]] >= 250:
                winner = text[i + 1]
                key_materials[text[i + 1]] -= 250
                break
        else:
            validate_key_existing(junk, text[i + 1])
            junk[text[i + 1]] += int(text[i])

print(f"{legendary_item[winner]} obtained!")

key_materials = dict(sorted(key_materials.items(), key=lambda x: (-x[1], x[0])))
junk = dict(sorted(junk.items()))
key_materials.update(junk)
for key, value in key_materials.items():
    print(f"{key}: {value}")
# for key, value in junk.items():
#     print(f"{key}: {value}")
