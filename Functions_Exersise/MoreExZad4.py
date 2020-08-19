def next_num(list):
    if len(list)>3:
        list.append(list[len(list)-1] + list[len(list)-2] + list[len(list)-3])
    elif len(list)>2:
        list.append(list[len(list)-1] + list[len(list)-2])
    else:
        list.append(list[len(list) - 1])
    return list

num = int(input())
print(next_num(num))