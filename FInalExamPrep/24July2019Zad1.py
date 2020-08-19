concert = {}
total_play = 0
while True:
    command = input()
    if command == "start of concert":
        break
    command = command.split("; ")
    band = command[1]
    if command[0] == "Add":
        members = command[2].split(", ")
        if band not in concert.keys():
            concert[band] = [members, 0]
        else:
            for each in members:
                if each not in concert[band][0]:
                    concert[band][0].append(each)
    elif command[0] == "Play":
        if band not in concert.keys():
            concert[band] = [[],int(command[2])]
            total_play += int(command[2])
        else:
            concert[band][1] += int(command[2])
            total_play += int(command[2])

band_name_to_print = input()

concert = dict(sorted(concert.items(), key=lambda x: (-x[1][1], x[0])))
print(f"Total time: {total_play}")
for k, v in concert.items():
    print(f"{k} -> {v[1]}")

print(band_name_to_print)
for each in concert[band_name_to_print][0]:
    print(f"=> {each}")




    #     if command[1] not in concert.keys():
    #         concert[command[1]] = [[each for each in members if each not in concert[command[1]]], 0]
    #     else:
    #         concert[command[1]] = [[concert[command[1]].append(each) for each in members if each not in concert[command[1]]], concert[command[1]]]
    # elif command[0] == "Play":
    #