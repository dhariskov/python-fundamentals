n = int(input())

students = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

display_students = {}
for key, value in students.items():
    if sum(value) / len(value) >= 4.5:
        display_students[key] = sum(value) / len(value)

display_students = dict(sorted(display_students.items(), key=lambda x: -x[1]))
for key, value in display_students.items():
    print(f"{key} -> {value:.2f}")

