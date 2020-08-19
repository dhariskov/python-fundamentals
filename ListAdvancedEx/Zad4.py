

rooms = int(input())
free_chairs = 0
flag =True
for i in range(rooms):
    string_chairs = input().split(" ")
    if len(string_chairs[0])<int(string_chairs[1]):
        print(f"{int(string_chairs[1])-len(string_chairs[0])} more chairs needed in room {i+1}")
        flag = False
    else:
        free_chairs+=len(string_chairs[0])-int(string_chairs[1])
if flag:
    print(f"Game On, {free_chairs} free chairs left")

