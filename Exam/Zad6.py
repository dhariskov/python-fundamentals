location_count = int(input())

expected_gold_amount = 0
gold_counter = 0
gold_per_day = 0
for i in range(location_count):
    expected_gold_amount = float(input())
    days_count = int(input())

    for j in range(days_count):
        gold_per_day = float(input())
        gold_counter += gold_per_day

    if expected_gold_amount <= gold_counter/days_count:
        print(f"Good job! Average gold per day: {gold_counter / days_count:.2f}.")
    else:
        print(f"You need {(expected_gold_amount - (gold_counter / days_count)):.2f} gold.")
    gold_counter = 0
