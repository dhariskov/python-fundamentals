n1 = float(input())
n2 = float(input())
n3 = float(input())

def count_sign(n1, n2, n3):
    negative = 0
    positive = 0
    my_list=[0, 0]
    if n1==0 or n2 ==0 or n3 ==0:
        return "zero"
    else:
        if n1<0:
            negative+=1
        else:
            positive+=1
        if n2<0:
            negative+=1
        else:
            positive+=1
        if n3<0:
            negative+=1
        else:
            positive+=1
        my_list[0]=negative
        my_list[1]=positive
        return my_list
if count_sign(n1,n2,n3) == "zero":
    print("zero")
elif count_sign(n1,n2,n3)[0]==1 or count_sign(n1,n2,n3)[0]==3:
    print("negative")
else:
    print("positive")