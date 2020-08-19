year = int(input())

flag=True
digits_of_year = None

while flag:
    year += 1
    digits_of_year=set(str(year))
    if len(digits_of_year)==len(str(year)):
        flag=False
        print(year)
