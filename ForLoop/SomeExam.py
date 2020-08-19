import sys
ticket_number = ""
min_stay_temp = sys.maxsize
flag_ticket_number = ""
flag_price = 0

while ticket_number != "End":
    ticket_number = input()
    if ticket_number == "End":
        break

    price = int(input())
    min_stay = int(input())

    if min_stay < min_stay_temp:
        min_stay_temp = min_stay
        flag_ticket_number = ticket_number
        flag_price = price

hour = min_stay_temp // 60
minutes = min_stay_temp % 60
print(f"Ticket found for flight {flag_ticket_number} costs {flag_price * 1.96:.2f} leva with {hour}h {minutes}m stay")
