import re
n = int(input())

pattern = r"^[!]([A-Z][a-z]{2,})[!][:][\[]([A-Za-z]{8,})[\]]$"

for _ in range(n):
    message = input()
    match = re.findall(pattern,message)
    if match == []:
        print("The message is invalid")
    else:
        encoded = ""
        for ch in match[0][1]:
            encoded += f"{str(ord(ch)) + ' '}"
        print(f"{match[0][0]}: {encoded}")
