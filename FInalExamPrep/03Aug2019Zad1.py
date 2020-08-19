text = input()

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    if command[0] == "Translate":
        text = text.replace(command[1], command[2])
        print(text)
    elif command[0] == "Includes":
        print(command[1] in text)
    elif command[0] == "Start":
        print(command[1] == text[0:len(command[1])])
    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif command[0] == "FindIndex":
        for i in range(-1, -len(text) -1, -1):
            if command[1] == text[i]:
                print(i + len(text))
                break
    elif command[0] == "Remove":
        remove = text[int(command[1]):int(command[1]) + int(command[2])]
        text = text.replace(remove, "")
        print(text)


