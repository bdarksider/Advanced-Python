# event loop(scheduler)
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

def g_fib(n):
    for x in range(1, n+1):
        yield fib(x)

from collections import deque
t = [g_fib(3), g_fib(5)]
