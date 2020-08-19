target = int(input())

command = ""
service = ""
money_counter = 0
haircut_type = ""
color_type = ""

while command != "closed":
    if money_counter >= target:
        print("You have reached your target for the day!")
        break

    command = input()
    if command == "haircut":
        haircut_type = input()
        if haircut_type == "mens":
            money_counter += 15
        elif haircut_type == "ladies":
            money_counter += 20
        elif haircut_type == "kids":
            money_counter += 10
    elif command == "color":
        color_type = input()
        if color_type == "touch up":
            money_counter += 20
        elif color_type == "full color":
            money_counter += 30
if money_counter < target:
    print(f"Target not reached! You need {target - money_counter}lv. more.")
print(f"Earned money: {money_counter}lv.")
