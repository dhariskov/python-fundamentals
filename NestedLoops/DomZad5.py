a = int(input())
b = int(input())

for i in range(a, b + 1):
    temp=str(i)
    num1 = (str(temp[0]))
    num2 = (str(temp[1]))
    num3 = (str(temp[2]))
    num4 = (str(temp[3]))
    num5 = (str(temp[4]))
    if int(num1) + int(num2) == int(num4) + int(num5):
        print(i,end=" ")
    else:
        if int(num1) + int(num2) < int(num4) + int(num5):
            temp2=int(num1) + int(num2) + int(num3)
            temp3= int(num4) + int(num5)
        else:
            temp2 = int(num1) + int(num2)
            temp3 = int(num4) + int(num5) + int(num3)
        if temp2 == temp3:
            print(i, end=" ")