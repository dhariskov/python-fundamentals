events=input().split("|")

energy = 100
coins = 100
counter=0
for each in events:
    event_or_ingredient=each.split("-")
    if event_or_ingredient[0] == "rest":
        energy+=int(event_or_ingredient[1])
        if energy>100:
            energy-=int(event_or_ingredient[1])
            print(f"You gained {100-energy} energy.")
            energy=100
        else:
            print(f"You gained {event_or_ingredient[1]} energy.")
        print(f"Current energy: {energy}.")
    elif event_or_ingredient[0]=="order":
        if energy>=30:
            energy-=30
            coins += int(event_or_ingredient[1])
            print(f"You earned {event_or_ingredient[1]} coins.")
        else:
            energy+=50
            print("You had to rest!")
    else:
        coins-=int(event_or_ingredient[1])
        if coins<=0:
            print(f"Closed! Cannot afford {event_or_ingredient[0]}.")
            break
        else:
            print(f"You bought {event_or_ingredient[0]}.")
    counter+=1
if counter == len(events):
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')