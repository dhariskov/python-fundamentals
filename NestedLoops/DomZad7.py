n = int(input())

presentation = input()
marks = 0
marks_counter = 0
average_mark = 0
average_all = 0
marks_counter_all = 0
counter_presentations = 0

while presentation != "Finish":
    marks_counter = 0
    counter_presentations += 1
    for i in range(0, n):
        marks = float(input())
        marks_counter += marks
        marks_counter_all += marks
    average_mark = marks_counter / n
    print(f"{presentation} - {average_mark:.2f}.")
    presentation = input()
average_all = marks_counter_all / (n * counter_presentations)
print(f"Student's final assessment is {average_all:.2f}.")
