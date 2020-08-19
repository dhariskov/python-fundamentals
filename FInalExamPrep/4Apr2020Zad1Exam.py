text = input()

while True:
    command = input()
    if command == "Generate":
        break
    command = command.split('>>>')
    if command[0] == "Contains":
        if command[1] in text:
            print(f"{text} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        temp = text[int(command[2]):int(command[3])]
        temp = eval(f"temp.{command[1].lower()}()")
        #username = eval(f"username.{command[1]}()")
        temp1 = text[0:int(command[2])]
        temp2 = text[int(command[3]):]
        text = temp1 + temp + temp2
        print(text)
    elif command[0] == "Slice":
        temp1 = text[0:int(command[1])]
        temp2 = text[int(command[2]):]
        text = temp1 + temp2
        print(text)
print(f"Your activation key is: {text}")