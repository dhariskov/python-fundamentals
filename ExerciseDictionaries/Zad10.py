submissions = {}
results = {}
while True:
    command = input()
    if command == "exam finished":
        break

    command = command.split("-")
    if "banned" in command:
        results.pop(command[0])
    else:
        user = command[0]
        language = command[1]
        points = command[2]

        if language not in submissions:
            submissions[language] = [points]
        else:
            submissions[language].append(points)

        if user in results:
            results[user] = max(int(results[user]), int(points))
        else:
            results[user] = points

results = dict(sorted(results.items(), key=lambda x: (-int(x[1]), x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-len(x[1]), x[0])))
print("Results:")
for k, v in results.items():
    print(f"{k} | {v}")
print("Submissions:")
for k, v in submissions.items():
    print(f"{k} - {len(v)}")
