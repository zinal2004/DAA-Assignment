def find_factors(number):
    if number <= 0:
        return "The number should be a positive integer."

    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    return factors

number = int(input("Enter a positive integer: "))
result = find_factors(number)
print(f"The factors of {number} are: {result}")
