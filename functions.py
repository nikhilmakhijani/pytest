def fib(n):    # write Fibonacci series up to n
    """
    This function creates Fibonacci series

    Args:
        n (integer): A number
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(6)
