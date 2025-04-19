def fibonacci(n):
    """
    Function to print Fibonacci series up to n terms
    """
    # Initialize first two terms
    a, b = 0, 1
    
    # Check if number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    elif n == 1:
        print(a)
    else:
        print("Fibonacci series:")
        for i in range(n):
            print(a, end=" ")
            # Update values
            a, b = b, a + b

# Example usage:
# fibonacci(10) # This will print first 10 terms of fibonacci series