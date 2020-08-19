n = int(input())

sum = 0
flag= True
for i in range(n):
    litters_to_add = int(input())
    sum+=litters_to_add
    if sum>255 and flag:
        flag = False
        print("Insufficient capacity!")
        sum -= litters_to_add
print(sum)
