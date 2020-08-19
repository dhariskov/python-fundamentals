def sum_numbers(a, b):
    return a + b


def subtract(ab, c):
    return ab - c


def add_and_subtract(a, b, c):
    sum = sum_numbers(a, b)
    result = subtract(sum, c)
    return result
  # return subtract(sum_numbers(a, b), c)


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
