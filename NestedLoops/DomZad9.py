n = int(input())
l = int(input())

fifth_start = 0
print_value = ""
for first in range(1,n+1):
    for second in range(1, n+1):
        for third in range(97 , 97 + l):
            for forth in range(97, 97 + l):
                if first < second:
                    fifth_start = second + 1
                else:
                    fifth_start = first + 1
                for fifth in range (fifth_start, n + 1):
                    print_value = str(first) + str(second) + chr(third) + chr(forth) + str(fifth)
                    print(print_value, end=" ")
