# Factorial using a function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is", factorial(num))

# Factorial using lambda and reduce
from functools import reduce

factorial_lambda = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print("Factorial (lambda) of", num, "is", factorial_lambda(num))
