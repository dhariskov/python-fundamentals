n = int(input())
players_count = int(input())
group_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
total_food = food_per_day*players_count*n
total_water = water_per_day*players_count*n

for i in range(1, n + 1):
    energy_lost_per_day = float(input())
    group_energy -= energy_lost_per_day
    if group_energy <= 0:
        break
    if i % 2 == 0:
        group_energy = group_energy * 1.05
        total_water = total_water * 0.7
    if i % 3 == 0:
        total_food = total_food - (total_food / players_count)
        group_energy = group_energy * 1.10

food = food_per_day*players_count
water = water_per_day*players_count

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")