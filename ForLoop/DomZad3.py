import sys
n = int(input())

sum_odd= 0
min_odd = sys.maxsize
max_odd = -sys.maxsize

sum_even = 0
min_even= sys.maxsize
max_even= -sys.maxsize

for i in range(1,n+1):
    number=float(input())
    if i%2 ==1 :
        sum_odd+=number
        if min_odd>number :
            min_odd=number
        if max_odd<number:
            max_odd=number
    else:
        sum_even+=number
        if min_even>number :
            min_even=number
        if max_even<number:
            max_even=number

print(f"OddSum={sum_odd:.2f},")

if min_odd == sys.maxsize :
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")

if max_odd == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")

print(f"EvenSum={sum_even:.2f},")

if min_even== sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")

if max_even == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")
