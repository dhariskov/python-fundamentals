register = {}

while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course = command[0]
    name = command[1]
    if course not in register:
        register[course] = [name]
    else:
        register[course].append(name)

register = dict(sorted(register.items(), key=lambda x: -len(x[1])))

for v in register.values():
    v.sort()

for k, v in register.items():
    print(f"{k}: {len(v)}")
    for each in v:
        print(f"-- {each}")
