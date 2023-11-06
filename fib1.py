def fibonacci_recursive(n):
    if n < 0:
        return "Input should be a non-negative integer"
    elif n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Taking user input for n and validating non-negative input
n = int(input("Enter a non-negative integer for Fibonacci calculation: "))

for i in range(n):
    print(fibonacci_recursive(i))

result = fibonacci_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")
