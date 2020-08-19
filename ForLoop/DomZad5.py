n = int(input())

p1_temp = 0
p2_temp = 0
p3_temp = 0
p4_temp = 0
p5_temp = 0

for i in range(n):
    number = int(input())
    if number < 200:
        p1_temp+=1
    elif number < 400 :
        p2_temp+=1
    elif number < 600 :
        p3_temp+=1
    elif number < 800 :
        p4_temp+=1
    else :
        p5_temp+=1

print(f"{p1_temp/n*100:.2f}%")
print(f"{p2_temp/n*100:.2f}%")
print(f"{p3_temp/n*100:.2f}%")
print(f"{p4_temp/n*100:.2f}%")
print(f"{p5_temp/n*100:.2f}%")

