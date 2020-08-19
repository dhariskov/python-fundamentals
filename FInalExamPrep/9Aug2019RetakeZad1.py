username = input()

temp = ""
while True:
    command = input()
    if command == "Sign up":
        break

    command = command.split()
    if command[0] == "Case":
        username = eval(f"username.{command[1]}()")
        print(username)
    elif command[0] == "Reverse":
        if 0<=int(command[1])<len(username) and int(command[2])<len(username):
            temp = username[int(command[1]):int(command[2])+1]
            temp = temp[::-1]
            print(temp)
    elif command[0] == "Cut":
        if command[1] in username:
            username = username.replace(command[1], "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {command[1]}.")
    elif command[0] == "Replace":
        username = username.replace(command[1] , "*")
        print(username)
    elif command[0] == "Check":
        if command[1] in username:
            print("Valid")
        else:
            print(f"Your username must contain {command[1]}.")

