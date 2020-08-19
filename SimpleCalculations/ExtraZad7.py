x = float(input())
y = float(input())
h = float(input())

# Green paint
green_paint = ((2*(x*x) - 1.2*2) + (2*(x*y) - 2*(1.5*1.5)))/3.4
print(f"{green_paint:.2f}")
# Red paint
red_paint = ((2*(x*y)) + (2*(x*h/2)))/4.3
print(f"{red_paint:.2f}")
