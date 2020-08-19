presents = input().split()

command = [""]
while command != "No Money":
    if command[0]=="OutOfStock":
        for each in range(len(presents)):
            if command[1]==presents[each]:
                presents[each]="None"
    elif command[0]=="Required":
        if int(command[2])<len(presents):
            presents[int(command[2])]=command[1]
    elif command[0]== "JustInCase":
        if len(presents)>0:
            presents[-1]=command[1]
    command=input()

    if command!="No Money":
        command=command.split()

for present in presents:
    if present!="None":
        print(present, end=" ")
