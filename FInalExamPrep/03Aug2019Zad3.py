my_dict = {}

max_count = int(input())
users_count = 0
while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("=")
    if command[0] == "Add":
        if command[1] not in my_dict.keys():
            my_dict[command[1]] = [int(command[2]),int(command[3])]
            users_count += 1
    elif command[0] == "Message":
        if command[1] in my_dict.keys() and command[2] in my_dict.keys():
            my_dict[command[1]][0] += 1
            my_dict[command[2]][1] += 1
            if (my_dict[command[1]][0] + my_dict[command[1]][1]) >= max_count:
                print(f"{command[1]} reached the capacity!")
                my_dict.pop(command[1])
                users_count -= 1
            if (my_dict[command[2]][0] + my_dict[command[2]][1]) >= max_count:
                print(f"{command[2]} reached the capacity!")
                my_dict.pop(command[2])
                users_count -= 1
    elif command[0] == "Empty":
        if command[1] in my_dict.keys():
            my_dict.pop(command[1])
            users_count -= 1
        elif command[1] == "All":
            my_dict={}
            users_count = 0

print(f"Users count: {users_count}")
my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1][1], x[0])))
for k, v in my_dict.items():
    print(f"{k} - {sum(v)}")