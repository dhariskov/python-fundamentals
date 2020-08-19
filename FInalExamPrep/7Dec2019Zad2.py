import re

n = int(input())
temp = []
counter = 0
for i in range(n):
    email = input()
    temp = re.split(r"U\$|P@\$", email)
    if len(temp) != 5:
        print("Invalid username or password")
    else:
        if len(temp[1])>=3 and temp[1][0].isupper() and temp[1][1:].islower() and len(temp[3])>5 and temp[3][:5].isalpha() and temp[3][-1].isdigit():
            print("Registration was successful")
            print(f"Username: {temp[1]}, Password: {temp[3]}")
            counter += 1
        else:
            print("Invalid username or password")

print(f"Successful registrations: {counter}")
