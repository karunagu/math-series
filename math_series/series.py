# Function to calculate Fibonacci series value based on the position "n"
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

# Use fibonacci fucntion to calculate lucas
# def lucas(n):
#     return fibonacci(n-1) + fibonacci(n+1)


# Function to calculate lucus series value based on the position "n"
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)