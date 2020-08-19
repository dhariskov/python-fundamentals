exam_hour = int(input())
exam_min = int(input())
arrive_hour = int(input())
arrive_min = int(input())

arrive_time_in_min = arrive_hour * 60 + arrive_min
exam_time_in_min = exam_hour * 60 + exam_min

diff = exam_time_in_min - arrive_time_in_min

if diff == 0:
    print("On time")
elif 30 >= diff > 0:
    print("On time")
    print(f"{abs(diff)} minutes before the start")
elif 60 > diff > 30:
    print("Early")
    print(f"{abs(diff) % 60} minutes before the start")
elif diff >= 60:
    print("Early")
    if (abs(diff) % 60 > 10):
        print(f"{abs(diff) // 60}:{abs(diff) % 60} hours before the start")
    else:
        print(f"{abs(diff) // 60}:0{abs(diff) % 60} hours before the start")
elif -60 < diff < 0:
    print("Late")
    print(f"{abs(diff)} minutes after the start")
elif diff <= -60:
    print("Late")
    if (abs(diff) % 60 > 10):
        print(f"{abs(diff) // 60}:{abs(diff) % 60} hours after the start")
    else:
        print(f"{abs(diff) // 60}:0{abs(diff) % 60} hours after the start")
