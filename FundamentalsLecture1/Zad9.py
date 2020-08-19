budget = float(input())
floor_price_kg = float(input())
egg_price = 0.75*floor_price_kg
milk_price = 1.25*floor_price_kg/4

cozunac_price = floor_price_kg+egg_price+milk_price
cozunac_counter = 0
colored_eggs_counter = 0

while budget > cozunac_price:
    budget-=cozunac_price
    cozunac_counter+=1
    colored_eggs_counter+=3
    if cozunac_counter%3==0:
        colored_eggs_counter-=cozunac_counter-2

total_money_spend=cozunac_counter*cozunac_price
print( f"You made {cozunac_counter} cozonacs! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")