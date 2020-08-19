record = float(input())
disntace = float(input())
time_for_meter = float(input())

time_without_slowing = disntace*time_for_meter
mid_slow_time = (disntace//15)*12.5

if record<= time_without_slowing+mid_slow_time:
    print(f"No, he failed! He was {((time_without_slowing+mid_slow_time) - record):.2f} seconds slower.")
else :
    print(f"Yes, he succeeded! The new world record is {((time_without_slowing+mid_slow_time)):.2f} seconds.")

