import re
pattern = r"([#\$%\*&])([A-za-z]+)\1[=]([\d]+)[!][!](.*)"

geolocation = ""
command = input()
while command :
    match = re.findall(pattern, command)
    if match == [] or (int(match[0][2]) != len(match[0][3])):
        print("Nothing found!")
    else:
        for ch in match[0][3]:
            geolocation += chr(ord(ch) + int(match[0][2]))
        print(f"Coordinates found! {match[0][1]} -> {geolocation}")
        geolocation = ""
        break
    command = input()