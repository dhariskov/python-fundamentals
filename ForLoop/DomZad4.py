n = int(input())

sum1 = 0
sum2 = 0
temp_sum = 0
temp_diff = 0
for i in range(0, n):
    if i % 2 == 0:
        number1 = int(input())
        number2 = int(input())
        sum1 = number1 + number2
    if i % 2 == 1:
        number1 = int(input())
        number2 = int(input())
        sum2 = number1 + number2
        if sum1 == sum2:
            temp_sum1 = sum1
        else:
            temp_diff = abs(sum1 - sum2)
    if n == 1:
        sum2 = 0
        temp_diff = abs(sum1 - sum2)
    if n == 1:
        sum2 = sum1
if sum1 == sum2:
    print(f"Yes, value={sum1}")
else:
    print(f"No, maxdiff={temp_diff}")
