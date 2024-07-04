def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result

n = int(input("Enter a non-negative integer: "))
result = factorial(n)
print(f"The factorial of {n} is {result}.")
