wiskey_price_liter = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
wiskey_liters = float(input())

rakia_price_liter = wiskey_price_liter/2
wine_price_liter = rakia_price_liter - rakia_price_liter*0.4
beer_price_liter = rakia_price_liter - rakia_price_liter*0.8

total =wiskey_price_liter*wiskey_liters + rakia_price_liter*rakia_liters + wine_price_liter*wine_liters + beer_liters*beer_price_liter
print(f"{total:.2f}")
