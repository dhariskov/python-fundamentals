def is_perfect(n):
    sum_proper_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_proper_divisors += i
    if sum_proper_divisors == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


num = int(input())
print(is_perfect(num))
