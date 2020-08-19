import re

n = int(input())
pattern = r"(.+)[>]([\d]{3}\|[a-z]{3}\|[A-Z]{3}\|([^<>]){3})[<]\1"
for i in range(n):
    password = input()
    match = re.findall(pattern, password)
    if match == []:
        print("Try another password!")
    else:
        result = match[0][1].replace("|","")
        print(f"Password: {result}")