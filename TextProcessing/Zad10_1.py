tickets = input()
tickets = tickets.replace(",", "").split()


def check(ticket, symbol, length=9):
    if symbol * length in ticket[:10] and symbol * length in ticket[10:20]:
        print(f'ticket "{ticket}" - {length}{symbol}')
    else:
        if length < 6:
            print(f'ticket "{ticket}" - no match')
        else:
            check(ticket, symbol, length - 1)


for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if ticket[4] not in "@#$^" or ticket[14] not in "@#$^" or (ticket[4] != ticket[14]):
            print(f'ticket "{ticket}" - no match')
        elif ticket[:10] == ticket[10:20] and len(set(ticket)) == 1:
            print(f'ticket "{ticket}" - {10}{ticket[0]} Jackpot!')
        else:
            check(ticket, ticket[4])
