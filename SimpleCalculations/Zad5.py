import math
# l = float(input())
# w = float(input())
# a = float(input())
#
# hall_area = l * w
# wadrope_area = a * a
#
# free_area = hall_area - wadrope_area - hall_area/10
# dancer_area = (7000 + 40)/10000
# dancers_count = free_area / dancer_area
#
# print(f"{round(dancers_count)}")


l = float(input())
w = float(input())
a = float(input())

hall_area = l*100 * w*100
wardrobe_area = a*100 * a*100

free_area = hall_area - wardrobe_area - hall_area/10
dancer_area = 7000 + 40
dancers_count = free_area / dancer_area
print(f"{math.floor(dancers_count)}")
