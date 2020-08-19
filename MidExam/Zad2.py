health = 100
bitcoins = 0
dungeons_rooms = input().split("|")
get_current_index = 0
is_dead = False
for command in dungeons_rooms:
    get_current_index = dungeons_rooms.index(command)
    command = command.split(" ")
    if command[0] == "potion":
        actual_healed = int(command[1])
        if health + actual_healed > 100:
            actual_healed = 100 - health
        health += actual_healed
        print(f"You healed for {actual_healed} hp.")
        print(f"Current health: {health} hp.")
    elif command[0] == "chest":
        bitcoins += int(command[1])
        print(f"You found {int(command[1])} bitcoins.")
    else:
        health -= int(command[1])
        if health > 0:
            print(f"You slayed {command[0]}.")
        else:
            print(f"You died! Killed by {command[0]}.")
            print(f"Best room: {get_current_index + 1}")
            is_dead = True
            break

if not is_dead:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
