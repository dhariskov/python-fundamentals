my_dict = {}

while True:
    flag = False
    flag1 = False
    command = input()
    force_user = ""
    force_side = ""
    if command == "Lumpawaroo":
        break
    if " | " in command:
        command = command.split(" | ")
        force_side = command[0]
        force_user = command[1]
        if force_side not in my_dict:
            my_dict[force_side] = [force_user]
        for each in my_dict.values():
            if force_user in each:
                flag1 = True
        if flag1 == False:
            my_dict[force_side].append(force_user)
    if " -> " in command:
        command = command.split(" -> ")
        force_user = command[0]
        force_side = command[1]

        if force_side not in my_dict:
            my_dict[force_side] = []
        for users in my_dict.values():
            if force_user in users:
                users.remove(force_user)
                my_dict[force_side].append(force_user)
                flag = True
        if flag == False:
            my_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for each in my_dict.values():
    each.sort()

my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
# my_dict = dict(sorted(my_dict.items(), key= lambda x: x[0]))


for key, val in my_dict.items():
    if len(val) > 0:
        print(f"Side: {key}, Members: {len(val)}")
    for each in val:
        print(f"! {each}")
