import re

n = int(input())
pattern = r"^([\$%])([A-Z][a-z]{2,})\1[:][\s][\[]([\d]+)[\]][\|][\[]([\d]+)[\]][\|][\[]([\d]+)[\]][\|]$"
for _ in range(n):
    message = input()
    match = re.findall(pattern, message)
    if match == []:
        print("Valid message not found!")
    else:
        char1 = chr(int(match[0][2]))
        char2 = chr(int(match[0][3]))
        char3 = chr(int(match[0][4]))
        printer = char1 + char2 + char3
        print(f"{match[0][1]}: {printer}")
