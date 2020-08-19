text = input()

my_list = []
for ch in text:
    my_list.append(ch)

power = 0
for i in range(len(my_list)):
    if my_list[i] == ">":
        power += int(my_list[i + 1])
    elif power > 0:
        my_list[i] = ""
        power -= 1

print("".join(my_list))

