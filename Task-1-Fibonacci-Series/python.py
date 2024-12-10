def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage
fib = fibonacci_generator()
for _ in range(10):  # Generate the first 10 Fibonacci numbers
    print(next(fib))