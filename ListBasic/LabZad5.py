cards_list=input().split()
number = int(input())

mid = int(len(cards_list)/2)
step=0
for j in range(number):
    step = 0
    second_list = [""] * len(cards_list)
    for i in range(mid):
        second_list[i+step]=cards_list[i]
        step +=1
        second_list[step+i] = cards_list[i+mid]
    cards_list=second_list
print(second_list)