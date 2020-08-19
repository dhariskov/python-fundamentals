import math
income = float(input())
mid_rate = float(input())
min_salary = float(input())


if mid_rate >= 4.5 and mid_rate < 5.5 and income < min_salary :
    social_scholarship = min_salary * 0.35
    print(f"You get a Social scholarship {math.floor(social_scholarship)} BGN")
elif mid_rate>=5.5 and income >= min_salary :
    print(f"You get a scholarship for excellent results {math.floor(25*mid_rate)} BGN")
elif mid_rate>=5.5 and income < min_salary :
    if min_salary * 0.35 <= 25*mid_rate :
        print(f"You get a scholarship for excellent results {math.floor(25 * mid_rate)} BGN")
    else :
        print(f"You get a Social scholarship {math.floor(min_salary * 0.35)} BGN")
else :
    print("You cannot get a scholarship!")