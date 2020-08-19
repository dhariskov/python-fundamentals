import math
lemon_weight = float(input())
sugar_kg = float(input())
water_kg = float(input())

lemon_juice = lemon_weight*980 + water_kg*1000 + sugar_kg*1000*0.3
cups=math.floor(lemon_juice/150)
money=cups*1.2

print(lemon_juice)
print(f"All cups sold: {(cups)}")
print(f"Money earned: {money:.2f}")