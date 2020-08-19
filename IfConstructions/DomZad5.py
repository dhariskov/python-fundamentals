hour = int(input())
minutes = int(input())

if minutes>=45 :
    if hour<23 :
        if minutes + 15 > 69:
                print(f"{hour+1}:{(minutes+15)%60}")
        else :
                print(f"{hour + 1}:0{(minutes + 15) % 60}")
    else:
        if minutes + 15 == 60:
            print(f"0:0{(minutes + 15) % 60}")
        elif ((minutes + 15)% 60)<10 :
            print(f"0:0{(minutes + 15) % 60}")
        else :
            print(f"0:{(minutes + 15) % 60}")
else :
    print(f"{hour}:{(minutes + 15)}")