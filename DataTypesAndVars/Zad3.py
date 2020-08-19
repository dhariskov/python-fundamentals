number_of_people = int(input())
capacity = int(input())

if number_of_people%capacity>0:
    courses = number_of_people//capacity +1
else:
    courses = number_of_people // capacity

print(courses)
