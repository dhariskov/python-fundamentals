tickets = input().split(", ")

counter_for_match = 6
symbol = ""
counter_a = 0
counter_pound = 0
counter_up = 0
for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ("$" or "@" or "#" or "^" in (set(ticket))) and len(set(ticket)) == 1:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        elif False:
            pass
            print(f'ticket "{ticket}" - no match')
        else:
            for i in range(len(ticket) // 2 - 6):
                if ticket[i] == ticket[i + 6]:
                    counter_for_match += 1
                else:
                    if counter_for_match < 6:
                        counter_for_match = 1
            print(f'ticket "{ticket}" - {counter_for_match}{ticket[4]}')
