bad_marks_count = int(input())

mark = 0
problem=""
counter = 0
average_score = 0
bad_marks_counter = 0
flag_enough = ""
while problem !="Enough" or bad_marks_counter<bad_marks_count:
    flag_enough = problem
    problem = input()
    if problem=="Enough":
        print(f"Average score: {(average_score)/counter:.2f}")
        print(f"Number of problems: {counter}")
        print(f"Last problem: {flag_enough}")
        break

    mark= int(input())
    counter += 1
    average_score=average_score+mark
    if mark<=4 :
        bad_marks_counter+=1

    if bad_marks_counter==bad_marks_count:
        print(f"You need a break, {bad_marks_count} poor grades.")
        break


