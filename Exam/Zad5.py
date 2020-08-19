months = int(input())

electricity = 0
electricity_total = 0
other = 0
for i in range(months):
    electricity = float(input())
    electricity_total+=electricity
    other+=(20+15+electricity)*1.2

water = months*20
internet = months*15
total = electricity_total + water + internet + other
print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {total/months:.2f} lv")