my_dictionary = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in my_dictionary:
        my_dictionary[resource] = quantity
    else:
        my_dictionary[resource] += quantity

for key, value in my_dictionary.items():
    print(f"{key} -> {value}")




