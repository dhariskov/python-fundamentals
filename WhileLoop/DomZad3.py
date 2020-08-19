trip_money = float(input())
money_saved = float(input())

counter_spend = 0
counter_saved = 0
total_days = 0

while money_saved < trip_money:
    action=""
    action = input()
    money_over_action = float(input())
    total_days += 1
    if action == "spend":
        money_saved = money_saved - money_over_action
        if money_saved < 0:
            money_saved = 0
        counter_spend += 1
        if counter_spend == 5:
            break
    if action == "save":
        money_saved = money_saved + money_over_action
        counter_spend = 0


if counter_spend == 5:
    print("You can't save the money.")
    print(f"{total_days}")
if money_saved >= trip_money:
    print(f"You saved the money for {total_days} days.")
