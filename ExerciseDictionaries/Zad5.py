n = int(input())

parking = {}
for i in range(n):
    command = input().split(" ")
    if command[0] == "register":
        if command[1] not in parking:
            parking[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {command[2]}")
    elif command[0] == "unregister":
        if command[1] not in parking:
            print(f"ERROR: user {command[1]} not found")
        else:
            print(f"{command[1]} unregistered successfully")
            parking.pop(command[1])

for k, v in parking.items():
    print(f"{k} => {v}")