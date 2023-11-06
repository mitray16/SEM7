def fibonacci_non_recursive(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
n = int(input("enter number: "))

for i in range(n):
    print(fibonacci_non_recursive(i))

result = fibonacci_non_recursive(n)
print(f"The {n}th Fibonacci number is: {result}")

