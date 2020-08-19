string = input()
string = string.replace(".", "")
result = int(string) + 1
result = str(result)
result = result[0] + "." + result[1] + "." + result[2]
print(result.strip())
