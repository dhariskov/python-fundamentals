n = int(input())

counter1 = 0
counter2 = 0
counter3 = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        counter1 += 1
    if number % 3 == 0:
        counter2 += 1
    if number % 4 == 0:
        counter3 += 1

print(f"{counter1/n*100:.2f}%")
print(f"{counter2/n*100:.2f}%")
print(f"{counter3/n*100:.2f}%")
