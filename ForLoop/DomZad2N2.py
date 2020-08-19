n = int(input())
temp_sum1 = 0
temp_sum2 = 0
temp_diff = 0
diff = 0
flag = False
for i in range(n):

    number1 = int(input())
    number2 = int(input())

    if i % 2 == 0:
        temp_sum1 = number1 + number2
    else:
        temp_sum2 = number1 + number2

    if temp_sum1 == temp_sum2 or n == 1:
        flag = True
    else:
        temp_diff = abs(temp_sum1 - temp_sum2)
        flag = False
        if diff < temp_diff:
            diff = temp_diff

if flag == True:
    print(f"Yes, value={temp_sum1}")
else:
    print(f"No, maxdiff={temp_diff}")
