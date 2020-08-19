import re

text = input()
word = input()

regex = f"(?i){word}\\b"

match = re.findall(regex, text)

print(len(match))