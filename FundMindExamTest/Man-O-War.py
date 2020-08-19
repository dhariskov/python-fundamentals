pirate_ship = input().split(">")
worship = input().split(">")
max_health = int(input())
pirate_ship = list(map(int, pirate_ship))
worship = list(map(int, worship))


def is_valid_index(index, some_list):
    return 0 <= index < len(some_list)


pirate_ship_lost = False
worship_lost = False
while True:
    command = input()

    if command == "Retire":
        break

    command = command.split(" ")

    if command[0] == "Fire" and is_valid_index(int(command[1]), worship):
        worship[int(command[1])] -= int(command[2])
        if worship[int(command[1])] <= 0:
            print("You won! The enemy ship has sunken.")
            worship_lost = True
            break
    elif command[0] == "Defend" and is_valid_index(int(command[1]), pirate_ship) and \
            is_valid_index(int(command[2]), pirate_ship):
        for i in range(int(command[1]), int(command[2]) + 1):
            pirate_ship[i] -= int(command[3])
            if pirate_ship[i] <= 0:
                pirate_ship_lost = True
                print("You lost! The pirate ship has sunken.")
                break
        if pirate_ship_lost:
            break
    elif command[0] == "Repair" and is_valid_index(int(command[1]), pirate_ship):
        pirate_ship[int(command[1])] += int(command[2])
        if pirate_ship[int(command[1])] > max_health:
            pirate_ship[int(command[1])] = max_health
    elif command[0] == "Status":
        counter = 0
        for each in pirate_ship:
            if each < max_health * 0.2:
                counter += 1
        print(f"{counter} sections need repair.")

if not (worship_lost or pirate_ship_lost):
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(worship)}")
