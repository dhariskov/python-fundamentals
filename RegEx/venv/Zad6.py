import re

pattern = r"\b(([w]{3})([\.][A-Za-z0-9]+([-][A-Za-z0-9]+)*)*[\.][A-Za-z0-9]+([-][A-Za-z0-9]+)*[\.][A-Za-z]+)"
my_list = []
while True:
    text = input()
    if text == "":
        break
    match = re.findall(pattern,text)
    #print(match)
    if match != []:
        my_list.extend(match[0])

#print(my_list)
for i in range(0, len(my_list), 5):
    print(my_list[i])


