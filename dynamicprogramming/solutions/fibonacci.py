"""
Compute the nth element of the Fibonacci sequence using dynamic programming approach

Fn = Fn-1 + Fn-2
F1 = 1
F0 = 0
"""
from functools import lru_cache


def fibonacci_iterative(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib_prev_prev = 0
    fib_prev = 1
    fib_current = None

    for i in range(2, n+1):
        fib_current = fib_prev + fib_prev_prev
        fib_prev_prev = fib_prev
        fib_prev = fib_current

    return fib_current


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
