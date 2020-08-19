def add(list_add):
    exit_list = []
    for add, animal_name, daily_food, area in list_add:
        if add == "Add":
            exit_list.append([animal_name, daily_food, area])

    exit_list.sort()
    for i in range(len(exit_list) - 1):
        if exit_list[i][0] == exit_list[i + 1][0]:
            exit_list[i + 1][1] = str(int(exit_list[i][1]) + int(exit_list[i + 1][1]))
            exit_list[i][1] = str(0)

    for animal_name, daily_food, area in exit_list:
        if int(daily_food) <= 0:
            exit_list.remove([animal_name, daily_food, area])
    return exit_list


def feed(list_feed, add_list):
    for feed, animal_name, food, area in list_feed:
        if feed == "Feed":
            for i in range(len(add_list)):
                if animal_name == add_list[i][0]:
                    add_list[i][1] = str(int(add_list[i][1]) - int(food))

            for animal_name, food, area in add_list:
                if int(food) <= 0:
                    print(f"{animal_name} was successfully fed")
                    add_list.remove([animal_name, food, area])
    return add_list


def hungry_animals_by_area(add_list):
    temp = []
    count = 0
    for i in range(len(add_list)):
        temp.append([add_list[i][2], "1"])
    for i in range(len(temp) - 1):
        if temp[i][0] == temp[i + 1][0]:
            temp[i + 1][1] = str(int(temp[i + 1][1]) + int(temp[i][1]))
            temp[i][1] = "0"
    temp.sort(key=lambda x: x[1], reverse=True)
    for area, count in temp:
        if count != "0":
            print(f"{area} : {count}")


command = input().split(":")
animal_list = []
while command[0] != "Last Info":
    animal_list.append(command)
    command = input().split(":")

add_list = add(animal_list)
add_list = feed(animal_list, add_list)

add_list.sort(key=lambda x: x[1], reverse=True)
add_list.sort()
print("Animals:")
for i in range(len(add_list) - 1, -1, -1):
    print(f"{add_list[i][0]} -> {add_list[i][1]}g")
# print(add_list)

print("Areas with hungry animals:")
hungry_animals_by_area(add_list)
