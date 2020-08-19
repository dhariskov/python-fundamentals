fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0

print("Cells:")
for each in fires:
    temp_value = each.split(" = ")
    if temp_value[0] == "High" and 80 < int(temp_value[1]) < 126:
        water -= int(temp_value[1])
        total_fire += int(temp_value[1])
        effort += int(temp_value[1]) * 0.25
        if water < 0:
            water += int(temp_value[1])
            total_fire -= int(temp_value[1])
            effort -= int(temp_value[1]) * 0.25
        else:
            print(f"- {temp_value[1]}")
    elif temp_value[0] == "Medium" and 50 < int(temp_value[1]) < 81:
        water -= int(temp_value[1])
        total_fire += int(temp_value[1])
        effort += int(temp_value[1]) * 0.25
        if water < 0:
            water += int(temp_value[1])
            total_fire -= int(temp_value[1])
            effort -= int(temp_value[1]) * 0.25
        else:
            print(f"- {temp_value[1]}")
    elif temp_value[0] == "Low" and 0 < int(temp_value[1]) < 51:
        water -= int(temp_value[1])
        total_fire += int(temp_value[1])
        effort += int(temp_value[1]) * 0.25
        if water < 0:
            water += int(temp_value[1])
            total_fire -= int(temp_value[1])
            effort -= int(temp_value[1]) * 0.25
        else:
            print(f"- {temp_value[1]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
