dict_contest_pass = {}
while True:
    contest_pass = input()
    if contest_pass == "end of contests":
        break

    contest_pass = contest_pass.split(":")
    contest = contest_pass[0]
    pass_contest = contest_pass[1]
    if contest not in dict_contest_pass:
        dict_contest_pass[contest] = list(pass_contest)

while True:
    cpup = input()
    if cpup == "end of submissions":
        break

    cpup = contest_pass.split("=>")
    if cpup[0] in dict_contest_pass.keys():
        if cpup[1] in dict_contest_pass[cpup[0]]:
            if cpup[2] in dict_contest_pass[cpup[0]] and cpup[3] > dict_contest_pass[cpup[0]][2]
            dict_contest_pass[cpup[0]].extend([cpup[2],cpup[3]])
