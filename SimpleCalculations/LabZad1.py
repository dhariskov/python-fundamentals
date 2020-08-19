# name = input("Name: ")
# print(f"Hello {name}!")

# Zad2
# first_name = input()
# last_name = input()
# age = int(input())
# town = input()
#
# print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")

# Zad3
# side = int(input())
# area = side * side
#
# print(area)

# Zad4
# sm = float(input())
# inch = 2.54
#
# print(f"{sm*inch:.2f}")

# Zad 5
# name = input()
# project_count = int(input())
# hours = 3*project_count
#
# print(f"The architect {name} will need {hours} hours to complete {project_count} project/s.")

# Zad 6
# import math
# r = float(input())
#
# s = math.pi*r*r
# p = 2*math.pi*r
#
# print(f"{s:.2f}")
# print(f"{p:.02f}")

# Zad7
# dog_count = int(input())
# other_pets_count = int(input())
#
# total=dog_count*2.50 + other_pets_count*4
# print(f"{total:.02f} lv.")


# Zad8
# area = float(input())
#
# discount = area*0.18*7.61
# final_price = area*7.61 - discount
# print(f"The final price is: {final_price:.02f} lv.")
# print(f"The discount is: {discount:.02f} lv.")

# Zad9
lenght = int(input())
width = int(input())
heigh = int(input())
pecentage_already_used = float(input())

volume=lenght*heigh*width
water_used = (volume-volume*pecentage_already_used/100)/1000
print(f"{water_used:.03f}")



