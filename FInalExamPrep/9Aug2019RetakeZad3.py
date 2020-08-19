my_dict = {}
counter_followers = 0
while True:
    command = input()
    if command == "Log out":
        break
    command = command.split(":")
    if command[0] == "New follower":
        if command[1] not in my_dict.keys():
            counter_followers += 1
            my_dict[command[1]] = [0, 0]
    elif command[0] == "Like":
        if command[1] not in my_dict.keys():
            counter_followers += 1
            my_dict[command[1]] = [int(command[2]), 0]
        else:
            my_dict[command[1]][0] += int(command[2])
    elif command[0] == "Comment":
        if command[1] not in my_dict.keys():
            counter_followers += 1
            my_dict[command[1]] = [0, 1]
        else:
            my_dict[command[1]][1] += 1
    elif command[0] == "Blocked":
        if command[1] not in my_dict.keys():
            print(f"{command[1]} doesn't exist.")
        else:
            my_dict.pop(command[1])
            counter_followers -= 1

my_dict = dict(sorted(my_dict.items(), key=lambda x:  (-x[1][0], x[0])))
print(f"{counter_followers} followers")
for k, v in my_dict.items():
    print(f"{k}: {sum(v)}")
