num = input()

for digit in reversed(str(num)):
    for symbol in range (int(digit)):
        print(chr(int(digit)+33), end="")
    if int(digit) == 0:
        print("ZERO", end="")
    print()

