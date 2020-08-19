users = input().split(", ")

for each in users:
    flag1 = False
    flag2 = False
    if 3<=len(each)<=16:
        flag1 = True

    for ch in each:
        if 65<=ord(ch.upper())<=90 or ch == "-" or ch == "_" or 48<=ord(ch.upper())<=57:
            flag2 = True
        else:
            flag2 = False
            break
    if flag1 and flag2:
        print(each)


