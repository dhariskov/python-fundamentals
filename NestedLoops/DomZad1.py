a = int(input())
b = int(input())
c = int(input())
d = int(input())

for one_one in range (a, b + 1):
    for one_two in range (a, b + 1):
        for two_one in range (c, d + 1):
            for two_two in range(c, d + 1):
                if one_one + two_two == two_one + one_two and one_one != one_two and two_two!=two_one :
                    print(f"{one_one}{one_two}")
                    print(f"{two_one}{two_two}\n")