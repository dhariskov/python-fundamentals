step_counter = 0
while step_counter < 10000:
    steps_during_walk = input()
    if steps_during_walk == "Going home":
        steps_to_home = int(input())
        step_counter = step_counter + steps_to_home
        break
    else:
        step_counter += int(steps_during_walk)

if step_counter >= 10000:
    print("Goal reached! Good job!")
if steps_during_walk == "Going home" and step_counter < 10000:
    print(f"{10000 - step_counter} more steps to reach goal.")
