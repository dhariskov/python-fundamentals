input_1 = input().split(", ")
input_2 = input()

temp = []
#  #if each in input_2:
    #    temp.append(each)
    #
[temp.append(each) for each in input_1 if each in input_2]
#temp=set(temp)
#temp = list(temp)
print(temp)

