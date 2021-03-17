import time
import sys

def factorial(n):
    ans = 1

    while n > 1:
        ans = ans * n
        n = n - 1
      
    return ans

def factorial_r(n):
    
    if n == 1: # Siempre es importante definir el 'caso base'
        return 1

    return n - factorial_r(n - 1)


if __name__ == '__main__':
    # n = 10_000

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(100000)
    print(sys.getrecursionlimit())

    n = 7_000

    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)