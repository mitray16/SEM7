def fibonacci_non_recursive(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Taking user input for n and validating non-negative input
n = int(input("Enter a non-negative integer for Fibonacci calculation: "))
for i in range(n):
    print(fibonacci_non_recursive(i))

result = fibonacci_non_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")
