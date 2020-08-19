def factorial(n):
    result = 1
    for i in range(1, n+1):
        result*=i
    return result

n1 = int(input())
n2 = int(input())
fact1 = factorial(n1)
fact2 = factorial(n2)
print(f"{fact1/fact2:.2f}")