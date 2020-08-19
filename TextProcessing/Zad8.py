string = input().split()
num = ""
final_result = 0

for each in string:
    result = 0
    num = each[1:-1]
    if each[0].isupper():
        result += int(num) / (ord(each[0]) - 64)
    elif each[0].islower():
        result += int(num) * (ord(each[0]) - 96)

    if each[-1].isupper():
        result -= (ord(each[-1]) - 64)
    elif each[-1].islower():
        result += (ord(each[-1]) - 96)

    final_result += result
print(f"{final_result:.2f}")
