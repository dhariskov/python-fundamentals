items_price_list = input().split("|")
budget=float(input())
total_profit = 0.00
total_money_items_sold = 0.00

for each in items_price_list:
    item_price = each.split("->")
    if item_price[0] == "Clothes" and float(item_price[1])<=50:
        budget-=float(item_price[1])
        if budget<0:
            budget+=float(item_price[1])
        else:
            item_new_price = float(item_price[1]) * 1.4
            total_money_items_sold+=item_new_price
            total_profit+= item_new_price - float(item_price[1])
            print(f"{item_new_price:.2f}", end=" ")
    elif item_price[0] == "Shoes" and float(item_price[1])<=35:
        budget -= float(item_price[1])
        if budget < 0:
            budget += float(item_price[1])
        else:
            item_new_price = float(item_price[1]) * 1.4
            total_money_items_sold += item_new_price
            total_profit += item_new_price - float(item_price[1])
            print(f"{item_new_price:.2f}", end=" ")
    elif item_price[0] == "Accessories" and float(item_price[1])<=20.50:
        budget -= float(item_price[1])
        if budget < 0:
            budget += float(item_price[1])
        else:
            item_new_price = float(item_price[1]) * 1.4
            total_money_items_sold += item_new_price
            total_profit += item_new_price - float(item_price[1])
            print(f"{item_new_price:.2f}", end=" ")
print()
print(f"Profit: {total_profit:.2f}")
if (total_money_items_sold+budget)<150:
    print("Time to go.")
else:
    print("Hello, France!")