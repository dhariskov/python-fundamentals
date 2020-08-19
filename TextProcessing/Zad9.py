string = input()

unique_symbols = ""
word = ""
num = ""
full_word = ""
i = 0

while i < len(string):
    while not string[i].isdigit():
        word += string[i]
        i += 1
    while string[i].isdigit():
        num += string[i]
        i += 1
        if i == len(string):
            break

    full_word += word.upper() * int(num)
    word = ""
    num = ""

unique_symbols = set(full_word)
print(f"Unique symbols used: {len(unique_symbols)}")
print(full_word)
