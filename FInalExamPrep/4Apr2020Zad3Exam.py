my_dict = {}
while True:
    city_pop_gold = input()
    if city_pop_gold == "Sail":
        break
    city_pop_gold = city_pop_gold.split("||")
    if city_pop_gold[0] not in my_dict.keys():
        my_dict[city_pop_gold[0]] = [int(city_pop_gold[1]), int(city_pop_gold[2])]
    else:
        my_dict[city_pop_gold[0]][0] += int(city_pop_gold[1])
        my_dict[city_pop_gold[0]][1] += int(city_pop_gold[2])

while True:
    event = input()
    if event == "End":
        break
    event = event.split("=>")
    if event[0] == "Plunder":
        my_dict[event[1]][0] -= int(event[2])
        my_dict[event[1]][1] -= int(event[3])
        print(f"{event[1]} plundered! {event[3]} gold stolen, {event[2]} citizens killed.")
        if my_dict[event[1]][0] <= 0 or my_dict[event[1]][1] <= 0:
            my_dict.pop(event[1])
            print(f"{event[1]} has been wiped off the map!")
    elif event[0] == "Prosper":
        if int(event[2])<0:
            print("Gold added cannot be a negative number!")
        else:
            my_dict[event[1]][1] += int(event[2])
            print(f"{event[2]} gold added to the city treasury. {event[1]} now has {my_dict[event[1]][1]} gold.")

if my_dict == {}:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    my_dict = dict(sorted(my_dict.items(), key=lambda x: (-x[1][1], x[0])))
    print(f"Ahoy, Captain! There are {len(my_dict)} wealthy settlements to go to:")
    for k, v in my_dict.items():
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")

