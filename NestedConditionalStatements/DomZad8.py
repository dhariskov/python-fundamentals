month = input()
nights = int(input())

studio = 0
apartment = 0

if nights <= 7:
    if month == "May" or month=="October" :
        studio = 50*nights
        apartment=65*nights
    elif month == "June" or month=="September" :
        studio = 75.2 * nights
        apartment = 68.7 * nights
    elif month == "July" or month=="August" :
        studio = 76 * nights
        apartment = 77 * nights
elif 14 >= nights > 7 :
    if month == "May" or month == "October":
        studio = 50 * nights * 0.95
        apartment = 65 * nights
    elif month == "June" or month == "September":
        studio = 75.2 * nights
        apartment = 68.7 * nights
    elif month == "July" or month == "August":
        studio = 76 * nights
        apartment = 77 * nights
elif nights > 14:
    if month == "May" or month == "October":
        studio = 50 * nights * 0.7
        apartment = 65 * nights * 0.9
    elif month == "June" or month == "September":
        studio = 75.2 * nights * 0.8
        apartment = 68.7 * nights * 0.9
    elif month == "July" or month == "August":
        studio = 76 * nights
        apartment = 77 * nights * 0.9

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")
