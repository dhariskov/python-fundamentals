budget = int(input())
season = input()
count1 = int(input())

loan = 0
if season == "Spring":
    loan = 3000
    if count1 <= 6:
        loan *= 0.9
    elif count1 <= 11:
        loan *= 0.85
    elif count1 > 11:
        loan *= 0.75
elif season == "Summer":
    loan = 4200
    if count1 <= 6:
        loan *= 0.9
    elif count1 <= 11:
        loan *= 0.85
    elif count1 > 11:
        loan *= 0.75
elif season == "Autumn":
    loan = 4200
    if count1 <= 6:
        loan *= 0.9
    elif count1 <= 11:
        loan *= 0.85
    elif count1 > 11:
        loan *= 0.75
elif season == "Winter":
    loan = 2600
    if count1 <= 6:
        loan *= 0.9
    elif count1 <= 11:
        loan *= 0.85
    elif count1 > 11:
        loan *= 0.75

if count1 % 2 == 0 and not season == "Autumn":
    loan *= 0.95

if budget>=loan :
    print(f"Yes! You have {budget-loan:.2f} leva left.")
else :
    print(f"Not enough money! You need {loan-budget:.2f} leva.")