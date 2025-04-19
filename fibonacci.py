def fibonacci(n):
    """
    Generate Fibonacci sequence up to nth term
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def main():
    # Example usage
    n = 10
    result = fibonacci(n)
    print(f"First {n} numbers of Fibonacci sequence:")
    print(result)

if __name__ == "__main__":
    main()