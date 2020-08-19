def validate_key_existing(dictionary, key, def_value=0):
    if each not in dictionary:
        dictionary[key] = def_value


def print_dict(dictionary, template):
    for key, value in dictionary.items():
        print(template.format(key, value))


text = "".join(input().split(" "))
dictionary = {}
for each in text:
    # if each not in dictionary:
    #     dictionary[each] = 1
    # else:
    #     dictionary[each] += 1
    validate_key_existing(dictionary, each)
    dictionary[each] += 1

print_dict(dictionary, "{} -> {}")
