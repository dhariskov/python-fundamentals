budget = float(input())
statist_count = int(input())
price_per_statist = float(input())
decor = budget*0.1

if statist_count > 150 : price_per_statist =  price_per_statist - price_per_statist*0.1

if decor + price_per_statist*statist_count > budget :
    print("Not enough money!")
    print(f"Wingard needs {((decor + price_per_statist*statist_count) - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget-(decor + price_per_statist*statist_count)):.2f} leva left.")