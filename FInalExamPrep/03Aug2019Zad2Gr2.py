import re

n = int(input())

pattern = r"([*\|@])([A-Z][a-z]{2,})\1[:][\s][\[]([A-Za-z]+)[\]][\|][\[]([A-Za-z]+)[\]][\|][\[]([A-Za-z]+)[\]][\|]$"
for _ in range(n):
    message = input()
    match = re.findall(pattern, message)
    if match == []:
        print("Valid message not found!")
    else:
        printer = str(ord(match[0][2])) + " " + str(ord(match[0][3])) + " " + str(ord(match[0][4]))
        print(f'{match[0][1]}: {printer}')
