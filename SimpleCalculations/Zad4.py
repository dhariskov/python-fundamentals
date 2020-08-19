tables = int(input())
table_lenght = float(input())
table_width = float(input())

cover_area = (table_lenght+0.60)*(table_width+0.60)
diamond_area = (table_lenght/2)*(table_lenght/2)

price_usd= cover_area*tables*7 + diamond_area*tables*9
price_lv = price_usd*1.85
print(f"{price_usd:.02f} USD")
print(f"{price_lv:.02f} BGN")
