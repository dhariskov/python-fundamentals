treasure_chest = input().split("|")


while True:
    command = input()
    if command == "Yohoho!":
        break

    command=command.split(" ")
    if command[0] == "Loot":
        for each in command[1::]:
            if each not in treasure_chest:
                treasure_chest.insert(0,each)
    elif command[0] == "Drop":
        if 0<=int(command[1])<len(treasure_chest):
            treasure_chest.append(treasure_chest.pop(int(command[1])))
    elif command[0] == "Steal":
        stolen_items = []
        if int(command[1])>len(treasure_chest):
            command[1]=len(treasure_chest)
        for i in range(len(treasure_chest)-1, len(treasure_chest)-int(command[1])-1,-1):
            stolen_items.append(treasure_chest.pop(i))
        stolen_items = stolen_items[::-1]
        print(", ".join(stolen_items))

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = 0
    for each in treasure_chest:
        average_treasure_gain +=len(each)
    average_treasure_gain=average_treasure_gain/len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")




