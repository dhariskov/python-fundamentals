text = input()

while True:
    command = input()
    if command == "Finish":
        break
    command = command.split()
    if command[0] == "Replace":
        text = text.replace(command[1], command[2])
        print(text)
    elif command[0] == "Cut":
        if 0 <= int(command[1]) < len(text) and 0 <= int(command[2]) < len(text):
            replacement = text[int(command[1]):int(command[2]) + 1]
            text = text.replace(replacement, "")
            print(text)
        else:
            print("Invalid indexes!")
    elif command[0] == "Make":
        text = eval(f"text.{command[1].lower()}()")
        print(text)
    elif command[0] == "Check":
        if command[1] in text:
            print(f"Message contains {command[1]}")
        else:
            print(f"Message doesn't contain {command[1]}")
    elif command[0] == "Sum":
        sum = 0
        if 0 <= int(command[1]) < len(text) and 0 <= int(command[2]) < len(text):
            for ch in text[int(command[1]): int(command[2]) +1 ]:
                sum += ord(ch)
            print(sum)
        else:
            print("Invalid indexes!")