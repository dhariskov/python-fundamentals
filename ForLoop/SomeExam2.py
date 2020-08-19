n = int(input())

ticket_temp = ""

for i in range(n):
    ticket_number = input()

    if len(ticket_number) == 4:
        if 65 <= ord(ticket_number[0]) <= 90:
            print("Seat decoded: " + ticket_number[0] + ticket_number[1] + ticket_number[2])
        else:
            print("Seat decoded: " + ticket_number[3] + ticket_number[1] + ticket_number[2])
    elif len(ticket_number) == 5 or len(ticket_number) == 6:
        print("Seat decoded: " + ticket_number[0] + str(ord(ticket_number[1])))
