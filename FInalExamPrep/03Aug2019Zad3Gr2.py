my_dict = {}

people_count = 0
while True:
    command = input()
    if command == "Results":
        break
    command = command.split(":")
    if command[0] == "Add":
        if command[1] not in my_dict.keys():
            my_dict[command[1]] = [int(command[2]), int(command[3])]
            people_count += 1
        else:
            my_dict[command[1]][0] += int(command[2])
    elif command[0] == "Attack":
        if command[1] in my_dict.keys() and command[2] in my_dict.keys():
            my_dict[command[2]][0] -= int(command[3])
            if my_dict[command[2]][0] <= 0:
                my_dict.pop(command[2])
                people_count -= 1
                print(f"{command[2]} was disqualified!")
            my_dict[command[1]][1] -= 1
            if my_dict[command[1]][1] <= 0:
                my_dict.pop(command[1])
                people_count -= 1
                print(f"{command[1]} was disqualified!")
    elif command[0] == "Delete":
        if command[1] == "All":
            my_dict = {}
            people_count = 0
        else:
            if command[1] in my_dict.keys():
                my_dict.pop(command[1])
                people_count -= 1
my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1][0], x[0])))
print(f"People count: {people_count}")
for k, v in my_dict.items():
    print(f"{k} - {v[0]} - {v[1]}")