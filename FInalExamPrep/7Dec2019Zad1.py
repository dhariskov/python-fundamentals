email = input()
temp = ""
while True:
    command = input().split()
    if command[0] == "Complete":
        break
    elif command[0] == "Make":
        if command[1] == "Upper":
            email = email.upper()
            print(email)
        elif command[1] == "Lower":
            email = email.lower()
            print(email)
    elif command[0] == "GetDomain":
        for i in range(-1, -int(command[1]) - 1, -1):
            temp += email[i]
        print(temp[::-1])
        temp = ""
    elif command[0] == "GetUsername":
        if "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            for each in email:
                if each == "@":
                    break
                else:
                    temp += each
            print(temp)
            temp = ""
    elif command[0] == "Replace":
        email = email.replace(command[1], "-")
        print(email)
    elif command[0] == "Encrypt":
        for each in email:
            print(ord(each), end=" ")
