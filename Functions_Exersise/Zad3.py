def two_chars(a, b):
    string = ""
    for i in range(ord(a)+1, ord(b)):
        string += chr(i) + " "
    return string


a = input()
b = input()
print(two_chars(a, b))
