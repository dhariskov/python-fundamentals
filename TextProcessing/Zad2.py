string = input().split()
string.sort(key=lambda x: len(x))

result = 0
for i in range(len(string[0])):
    result += ord(string[0][i]) * ord(string[1][i])
if len(string[0]) < len(string[1]):
    for i in range(len(string[0]), len(string[1])):
        result += ord(string[1][i])
print(result)
