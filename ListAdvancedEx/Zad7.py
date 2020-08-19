sentence = input().split(" ")

char_to_convert = ""
for each in sentence:
    char_to_convert = ""
    for char in range(3):
        test=ord(each[char])
        if 48<=ord(each[char])<=57:
            char_to_convert +=each[char]
    first_letter = chr(int(char_to_convert))
    each = each[len(char_to_convert):]
    second_letter = each[-1]
    each=each[:-1]
    last_letter=""
    if len(each)>0:
        last_letter = each[0]
    each = each[1:]
    word = first_letter + second_letter + each + last_letter

    print(word, end=" ")
