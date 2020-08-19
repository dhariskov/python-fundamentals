factor = int(input())
count =  int(input())

list=[]
for i in range(factor, count*factor+1, factor):
    list.append(i)

print(list)