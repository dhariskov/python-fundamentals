def is_palindrome(list):
    temp=0
    for i in list:
        flag = True
        temp=len(i)//2
        for j in range(temp):
            if i[j] == i[-j-1]:
                flag=flag and True
            else:
                flag=flag and False
                break
        print(flag)


input = input().split(", ")
is_palindrome(input)