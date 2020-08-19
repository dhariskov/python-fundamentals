numbers = input().split(", ")
temp_list = []

for group in range(10, 101, 10):
    for each in numbers:
        if int(each) <= group:
            temp_list.append(each)
    temp_list = list(map(int, temp_list))
    print(f"Group of {group}'s: {temp_list}")
    temp_list = list(map(str, temp_list))
    numbers = [x for x in numbers if x not in temp_list]
    temp_list = []
    if len(numbers) == 0:
        break
