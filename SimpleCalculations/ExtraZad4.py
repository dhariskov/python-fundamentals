vegi_price_kg = float(input())
fruit_price_kg = float(input())
vegi_total_kg = int(input())
fruit_total_kg = int(input())

total = vegi_price_kg * vegi_total_kg + fruit_price_kg * fruit_total_kg
total /= 1.94
print(f"{total:.02f}")
