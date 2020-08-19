def exchange(numbers):
    index = command.split(" ")
    if int(index[1]) >= len(numbers) or int(index[1]) < 0:
        print("Invalid index")
    else:
        if int(index[1]) >= 0:
            for i in range(int(index[1]) + 1):
                numbers.append(numbers[i])
            del numbers[0:int(index[1]) + 1]
    return numbers


def even(numbers):
    evens = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            evens.append(numbers[i])
    return evens


def odd(numbers):
    odds = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            odds.append(numbers[i])
    return odds


def max_num(numbers, even_or_odd):
    if len(even_or_odd) > 0:
        result = max(even_or_odd)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == result:
                return i

    else:
        return "No matches"


def min_num(numbers, even_or_odd):
    if len(even_or_odd) > 0:
        result = min(even_or_odd)
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == result:
                return i
    else:
        return "No matches"


def first(command, numbers, even_or_odd):
    temp = []
    command = command.split(" ")
    if int(command[1]) > len(numbers):
        print("Invalid count")
    elif len(even_or_odd) == 0:
        print(temp)
    elif int(command[1]) >= len(even_or_odd):
        print(even_or_odd)
    else:
        for i in range(int(command[1])):
            temp.append(int(even_or_odd[i]))
        print(temp)


def last(command, numbers, even_or_odd):
    temp = []
    command = command.split(" ")
    if int(command[1]) > len(numbers):
        print("Invalid count")
    elif len(even_or_odd) == 0:
        print(temp)
    elif int(command[1]) >= len(even_or_odd):
        print(even_or_odd)
    else:
        even_or_odd.reverse()
        for i in range(int(command[1])):
            temp.append(int(even_or_odd[i]))
        temp.reverse()
        print(temp)


num = input().split(" ")
command = input()
for i in range(len(num)):
    num[i] = int(num[i])
while command != "end":
    if "exchange" in command:
        num = exchange(num)
    elif "max even" in command:
        print(max_num(num, even(num)))
    elif "max odd" in command:
        print(max_num(num, odd(num)))
    elif "min even" in command:
        print(min_num(num, even(num)))
    elif "min odd" in command:
        print(min_num(num, odd(num)))
    elif "first" in command and "even" in command:
        first(command, num, even(num))
    elif "last" in command and "even" in command:
        last(command, num, even(num))
    elif "first" in command and "odd" in command:
        first(command, num, odd(num))
    elif "last" in command and "odd" in command:
        last(command, num, odd(num))
    command = input()

print(num)
