n = int(input())

sum=0
biggest_num = 0
for i in range (0, n):
    number = int(input())
    if biggest_num<number:
        biggest_num=number

    sum+=number

sum-=biggest_num
if sum==biggest_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(biggest_num-sum)}")