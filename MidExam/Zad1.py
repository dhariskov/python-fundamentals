import math
students = int(input())
lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_bonus = 0
temp_attendances = 0
for i in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + additional_bonus)
    if max_bonus<total_bonus:
        max_bonus=total_bonus
        temp_attendances = attendances
print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {temp_attendances} lectures.")
