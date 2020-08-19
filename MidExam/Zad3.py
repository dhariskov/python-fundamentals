items = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break
    command = command.split(" - ")
    if command[0] == "Collect":
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == "Drop":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Combine Items":
        temp = command[1].split(":")
        if temp[0] in items:
            items.insert((items.index(temp[0]) + 1), temp[1])
    elif command[0] == "Renew":
        if command[1] in items:
            items.append(items.pop(items.index(command[1])))
print(", ".join(items))
