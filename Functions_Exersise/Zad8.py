def loading_bar(n):
    bar = ""
    temp = n // 10
    bar = "[" + temp * "%" + (10 - temp) * "." + "]"
    if temp == 10:
        return "100% Complete!\n " + bar
    else:
        return str(n) + "% " + bar + "\nStill loading..."


num = int(input())
print(loading_bar(num))
