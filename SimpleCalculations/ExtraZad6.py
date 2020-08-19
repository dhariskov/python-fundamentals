skumriq_price_kg = float(input())
caca_price_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price_kg = skumriq_price_kg + skumriq_price_kg*0.6
safrid_price= caca_price_kg + caca_price_kg*0.8

palamud_total_price=palamud_price_kg*palamud_kg
safrid_total_price=safrid_price*safrid_kg
midi_total_price=midi_kg*7.50

total= palamud_total_price + safrid_total_price + midi_total_price
print(f"{total:.2f}")
