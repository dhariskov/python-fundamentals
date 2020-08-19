own_money = float(input())
earned_money = float(input())
expenses = float(input())
present_price = float(input())

money_saved = 5 * (own_money + earned_money) - expenses

if money_saved >= present_price:
    print(f"Profit: {money_saved:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {(present_price - money_saved):.2f} BGN.")
