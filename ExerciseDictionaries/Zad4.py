from collections import defaultdict

products = defaultdict(str)

while True:
    command = input()
    if command == "buy":
        break

    command = command.split(" ")
    if command[0] not in products:
        products[command[0]] = command[0]
        products[command[0]] = [float(command[1]), int(command[2])]
    else:
        products[command[0]] = [float(command[1]), products[command[0]][1] + int(command[2])]

for key, val in products.items():
    print(f"{key} -> {val[0]*val[1]:.2f}")

