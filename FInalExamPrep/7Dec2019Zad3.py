
my_dict = {}

while True:
    command = input()
    if command == "Statistics":
        break
    command = command.split("->")
    if command[0] == "Add":
        if command[1] not in my_dict.keys():
            my_dict[command[1]] = []
        else:
            print(f"{command[1]} is already registered")
    elif command[0] == "Send":
        if command[1] in my_dict.keys():
            my_dict[command[1]].append(command[2])
    elif command[0] == "Delete":
        if command[1] in my_dict.keys():
            my_dict.pop(command[1])
        else:
            print(f"{command[1]} not found!")

my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), (x[0]))))
print(f"Users count: {len(my_dict)}")
for k, v in my_dict.items():
    print(k)
    for each in v:
        print(f" - {each}")