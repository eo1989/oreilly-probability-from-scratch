# Factorials multiply consecutive descending integers down to 1
# EXAMPLE: 5! = 5 * 4 * 3 * 2 * 1
def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

# Generates the coefficient needed for the binomial distribution
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k) * factorial(n - k))

print(f"FACTORIAL of 3: {factorial(3)}")
print(f"BINOMIAL COEFFICIENT n=3, k=2: {binomial_coefficient(3, 2)}")
