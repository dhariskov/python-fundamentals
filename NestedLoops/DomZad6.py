number = ""

counter = 0
prime_sum = 0
not_prime_sum = 0

while number != "stop":
    number = input()
    if number == "stop":
        break
    if int(number)<0:
        print("Number is negative.")
        continue
    counter = 0
    for i in range (1, int(number)+1):
        if int(number)%i==0:
            counter+=1
    if counter == 2:
        prime_sum += int(number)
    else:
        not_prime_sum += int(number)


print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")


