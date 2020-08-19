text = input()

while True:
    command = input()
    if command == 'Done':
        break
    command = command.split()
    if command[0] == 'Change':
        text = text.replace(command[1], command[2])
        print(text)
    elif command[0] == 'Includes':
        print(command[1] in text)
    elif command[0] == 'End':
        print(command[1][::-1] == text[len(text):len(text) - len(command[1]) - 1:-1])
    elif command[0] == 'Uppercase':
        text = text.upper()
        print(text)
    elif command[0] == 'FindIndex':
        for i in range(len(text)):
            if command[1] == text[i]:
                print(i)
                break
    elif command[0] == 'Cut':
        text = text[int(command[1]):int(command[1]) + int(command[2])]
        print(text)
