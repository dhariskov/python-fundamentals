degrees = float(input())

if degrees >= 5.00 and degrees < 11.99 :
    print("Cold")
elif degrees >= 12.00 and degrees <=14.99 :
    print("Cool")
elif degrees >= 15.00 and degrees <=20.00 :
    print("Mild")
elif degrees >= 20.1 and degrees <=25.9 :
    print("Warm")
elif degrees >= 26.00 and degrees <=35 :
    print("Hot")
else :
    print("unknown")