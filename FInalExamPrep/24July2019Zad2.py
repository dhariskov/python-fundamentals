import re

encrypted_song = ""
key = 0
pattern = r"^([A-Z][a-z]*[\s\'a-z]+)[:]([A-Z]+[\sA-Z]*)$"
while True:
    command = input()
    if command == "end":
        break
    match = re.findall(pattern, command)
    if not match:
        print("Invalid input!")
    else:
        key = len(match[0][0])
        for ch in match[0][0]:
            if ch not in " '":
                if ch.isupper():
                    encrypted_song += chr(((ord(ch) - 65 + key) % 26) + 65)
                else:
                    encrypted_song += chr(((ord(ch) - 97 + key) % 26) + 97)
            else:
                encrypted_song += ch
        encrypted_song += "@"
        for ch in match[0][1]:
            if ch not in " '":
                encrypted_song += chr(((ord(ch) - 65 + key) % 26) + 65)
            else:
                encrypted_song += ch
        print(f"Successful encryption: {encrypted_song}")
        encrypted_song = ""
