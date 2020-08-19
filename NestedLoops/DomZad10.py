n = int(input())

forth = 0
third = 0
second = 0
first = 0
temp_num = 0
flag = True

for i in range(1111, 10000):
    flag = True
    temp_num = i
    forth = temp_num % 10
    if forth==0:
        continue
        flag = False
    temp_num = temp_num // 10
    third = temp_num % 10
    if third==0:
        continue
        flag = False
    temp_num = temp_num // 10
    second = temp_num % 10
    if second==0:
        continue
        flag = False
    temp_num = temp_num // 10
    first = temp_num
    if second==0:
        continue
        flag = False
    if flag and (n % first == 0 and n % second == 0 and n % third == 0 and n % forth == 0):
        print(i, end=" ")
