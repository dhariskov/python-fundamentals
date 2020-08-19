minutes = int(input())
player_name = input()

if minutes == 0:
    print("Match has just began!")
elif minutes < 45:
    print("First half time.")
    if minutes <= 10:
        print(f"{player_name} missed a penalty.")
        if minutes % 2 == 0:
            print(f"{player_name} was injured after the penalty.")
    elif minutes <= 35:
        print(f"{player_name} received yellow card.")
        if minutes % 2 == 1:
            print(f"{player_name} got another yellow card.")
    elif minutes > 35:
        print(f"{player_name} SCORED A GOAL !!!")
elif minutes >= 45:
    print("Second half time.")
    if minutes > 45 and minutes <= 55 :
        print(f"{player_name} got a freekick.")
        if minutes % 2 == 0:
            print(f"{player_name} missed the freekick.")
    elif minutes> 55 and minutes <= 80:
        print(f"{player_name} missed a shot from corner.")
        if minutes % 2 == 1:
            print(f"{player_name} has been changed with another player.")
    elif minutes> 80 and minutes <= 90:
        print(f"{player_name} SCORED A GOAL FROM PENALTY !!!")
