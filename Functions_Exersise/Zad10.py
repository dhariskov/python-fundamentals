def exchange (command, numbers):
    index = command.split(" ")
    if int(index[1])>=len(numbers):
        print("Invalid index")
    else:
        for i in range(int(index[1])+1):
            numbers.append(numbers[i])
        del numbers[0:int(index[1])+1]
    return numbers


def max_min_even_odd(command, numbers):
    temp_list=[]
    result = None
    if command == "max even" or command == "min even":
        for i in range(len(numbers)):
            if int(numbers[i])%2==0:
                temp_list.append(numbers[i])
        if command == "max even" and len(temp_list)!=0:
            result = max(temp_list)
        elif command == "min even" and len(temp_list)!=0:
            result = min(temp_list)
    elif command == "max odd" or command == "min odd":
        for i in range(len(numbers)):
            if int(numbers[i])%2==1:
                temp_list.append(numbers[i])
        if command == "max odd" and len(temp_list)!=0:
            result = max(temp_list)
        elif command == "min odd" and len(temp_list)!=0:
            result = min(temp_list)
    if result is None:
        return "No matches"
    else:
        return numbers.index(result)


def first_last_even_odd (command, numbers):
    temp_list=[]
    command = command.split(" ")
    if int(command[1])>=len(numbers):
        return "Invalid count"
    if command[2] == "even":
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 == 0:
                temp_list.append(numbers[i])
    else:
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 == 1:
                temp_list.append(numbers[i])
    if command[0] == "first":
        if len(temp_list) == 0:
            print("[]")
        else:
            for j in range(len(temp_list)):
                print(f"{temp_list[j]}")
                if j==command[1]:
                    break
    elif command[0] == "last":
        if len(temp_list) == 0:
            print("[]")
        else:
            for j in range(len(temp_list), 0, -1):
               print(temp_list[j])
               if len(temp_list)<command[1]:
                   break


num = input().split(" ")
for i in range(len(num)):
    num[i] = int(num[i])
#print(num)


command = input()
while command != "end":
    execute = command.split(" ")
    if execute[0] == "exchange":
        num = exchange(command,num)
    elif command == "max even" or command == "max odd" or command == "min even" or command == "min odd":
        print(max_min_even_odd(command,num))
    elif execute[0] == "first" or execute[0] == "last":
        first_last_even_odd(command, num)

    command = input()
print(num)