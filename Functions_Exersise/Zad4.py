def sum_odd_even(n):
    sum_even = 0
    sum_odd = 0
    string = ""
    for i in range(len(n)):
        a = int(n[i])
        if a%2==0:
            sum_even += a
        else:
            sum_odd +=a
    string = "Odd sum = " + str(sum_odd) + ", Even sum = " + str(sum_even)
    return string

n = input()
print(sum_odd_even(n))
