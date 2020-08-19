import re

pattern = r"\d+"
text = input()
my_list = []
while text != "":
    match = re.findall(pattern,text)
    my_list.extend(match)
    text = input()

print(" ".join(my_list))
