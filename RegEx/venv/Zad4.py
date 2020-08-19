import re
text = input()
regex = r"(^| )[a-z0-9]+([\.\-_][a-z0-9]+)*@[a-z]+(-[a-z]+)*(\.[a-z]+(-[a-z]+)*)+"

match = re.finditer(regex,text)

for value in match:
    result = value[0].strip()
    print(result)
