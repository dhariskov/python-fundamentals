targets = input().split("|")

for i in range(len(targets)):
    targets[i] = int(targets[i])

temp = []
points_won = 0
while True:
    command = input()
    if command == "Game over":
        break
    temp = command.split("@")
    if temp[0] == "Shoot Left" and 0 <= int(temp[1]) < len(targets):
        index = (int(temp[1]) - int(temp[2])) % len(targets)
        if targets[index] >= 5:
            targets[index] = targets[index] - 5
            points_won += 5
        elif targets[index] > 0:
            points_won += targets[index]
            targets[index] = 0
    elif temp[0] == "Shoot Right" and 0 <= int(temp[1]) < len(targets):
        index = (int(temp[1]) + int(temp[2])) % len(targets)
        if targets[index] >= 5:
            targets[index] = targets[index] - 5
            points_won += 5
        elif targets[index] > 0:
            points_won += targets[index]
            targets[index] = 0
    elif temp[0] == "Reverse":
        targets = targets[::-1]
for i in range(len(targets)):
    targets[i] = str(targets[i])

result = " - ".join(targets)
print(result)
print(f"Iskren finished the archery tournament with {points_won} points!")
