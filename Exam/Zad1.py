tickets_to = float(input())
tickets_back = float(input())
mach_ticket = float(input())
count_mach = int(input())
discount = int(input())

tickets_total = 6*((tickets_to + tickets_back)-((tickets_to + tickets_back)* (discount/100)))
mach_tickets_total = 6 * mach_ticket * count_mach

sum_total = tickets_total + mach_tickets_total
price_per_person = sum_total / 6

print(f"Total sum: {sum_total:.2f} lv.")
print(f"Each friend has to pay {price_per_person:.2f} lv.")
