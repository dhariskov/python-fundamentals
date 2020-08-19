cards = input().split()

A = [1]*11
B = [1]*11

for elem in cards:
    if elem[0]=="A":
        A[int(elem.split("-")[-1])-1] = 0
    else:
        B[int(elem.split("-")[-1])-1] = 0

    #if sum_A<7 or sum_B<7:
    #    break
sum_A=sum(A)
sum_B=sum(B)
print(f"Team A - {sum_A}; Team B - {sum_B}")
if sum_A<7 or sum_B<7:
    print("Game was terminated")