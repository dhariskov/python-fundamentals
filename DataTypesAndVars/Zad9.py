import math
n = int(input())

list_snowballSnow =[]
list_snowballTime =[]
list_snowballQuality =[]
list_current_snowballValue=[]
biggest_elemet=0

for i in range(n):
    snowballSnow=int(input())
    list_snowballSnow.append(snowballSnow)
    snowballTime = int(input())
    list_snowballTime.append(snowballTime)
    snowballQuality= int(input())
    list_snowballQuality.append(snowballQuality)

    number = int(snowballSnow / snowballTime)
    current_snowballValue=0
    current_snowballValue = pow(number,snowballQuality)
    list_current_snowballValue.append(current_snowballValue)
    if biggest_elemet <current_snowballValue:
        biggest_elemet=current_snowballValue

#list_snowballSnow.sort(reverse=True)
#list_snowballTime.sort(reverse=True)
#list_snowballQuality.sort(reverse=True)
el=list_current_snowballValue.index(biggest_elemet)

#print(list_snowballSnow)
#print(list_snowballTime)
#print(list_snowballQuality)
#print(list_current_snowballValue)
#print(el)
#highest_current_snowballValue = 0
#highest_current_snowballValue=int(list_snowballSnow[0] / list_snowballTime[0]) ** list_snowballQuality[0]


print(f"{list_snowballSnow[el]} : {list_snowballTime[el]} = {biggest_elemet} ({list_snowballQuality[el]})")



