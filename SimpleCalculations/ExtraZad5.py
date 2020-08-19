import math
w = float(input())
h = float(input())

descs_in_w = w*100//120
desc_in_h = (h*100-100)//70

print(descs_in_w)
print(desc_in_h)
print(f"{round(descs_in_w*desc_in_h)-3}")

# hall_area = (w*100)*(h*100-100)
# desk_area = 70*120
# places= hall_area//desk_area - 3
# print(places)
# print(f"{math.floor(places)}")
