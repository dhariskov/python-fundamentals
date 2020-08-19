a = int(input())
b = int(input())

for i in range(a, b + 1):
    temp=str(i)
    num1 = (str(temp[0]))
    num2 = (str(temp[1]))
    num3 = (str(temp[2]))
    num4 = (str(temp[3]))
    num5 = (str(temp[4]))
    num6 = (str(temp[5]))
    if int(num1) + int(num3) + int(num5) == int(num2) + int(num4) + int(num6):
        print(i,end=" ")
