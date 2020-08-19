my_dict = {}
unliked_meals = 0
while True:
    command = input()
    if command == "Stop":
        break
    command = command.split('-')
    if command[0] == "Like":
        if command[1] not in my_dict.keys():
            my_dict[command[1]] = [command[2]]
        elif command[2] not in my_dict[command[1]]:
            my_dict[command[1]].append(command[2])
    elif command[0] == "Unlike":
        if command[1] not in my_dict.keys():
            print(f"{command[1]} is not at the party.")
        elif command[2] not in my_dict[command[1]]:
            print(f"{command[1]} doesn't have the {command[2]} in his/her collection.")
        else:
            my_dict[command[1]].remove(command[2])
            unliked_meals += 1
            print(f"{command[1]} doesn't like the {command[2]}.")

my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for k, v in my_dict.items():
    print(f"{k}: {', '.join([each for each in v])}")
print(f"Unliked meals: {unliked_meals}")