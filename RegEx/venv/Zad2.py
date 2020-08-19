import re

regex = r"\b_[A-Za-z/d]+\b"
regex2 = "[A-Za-z/d]+"
text = input()
match = re.findall(regex,text)
my_list = []
for i in range(len(match)):
    my_list.extend(re.findall(regex2, match[i]))

print(",".join(my_list))
