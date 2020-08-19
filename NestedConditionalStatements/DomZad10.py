import math
year = input()
p = int(input())
h = int(input())

plays_in_sofia = (48 - h)*3/4
plays_in_home = h
bank_holidays_plays = p * 2/3

total_plays = plays_in_sofia + plays_in_home + bank_holidays_plays

if year == "leap" :
    print(f"{math.floor(total_plays*1.15)}")
else :
    print(f"{math.floor(total_plays)}")
