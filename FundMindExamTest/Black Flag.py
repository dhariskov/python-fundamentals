days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
for i in range(1, days+1):
    total_plunder+=daily_plunder
    if i%3 == 0:
        total_plunder += 0.5*daily_plunder
    if i%5 == 0:
        total_plunder=total_plunder*0.7

if expected_plunder<=total_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {100*(total_plunder/expected_plunder):.2f}% of the plunder.")




