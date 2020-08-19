import re

threshold_pattern = r"\d"
emoji_pattern = r"([:]{2}|[\*]{2})([A-Z][a-z]{2,})\1"

text = input()

digits_match = re.findall(threshold_pattern, text)
emoji_match = re.findall(emoji_pattern, text)

if digits_match == []:
    threshold = 0
else:
    threshold = 1
    for digit in digits_match:
        threshold *= int(digit)

print(f"Cool threshold: {threshold}")
print(f"{len(emoji_match)} emojis found in the text. The cool ones are:")
emoji_coolnes = 0
for each in emoji_match:
    emoji_coolnes = 0
    for ch in each[1]:
        emoji_coolnes += ord(ch)
    if emoji_coolnes >= threshold:
        print(f"{each[0]}{each[1]}{each[0]} ")


