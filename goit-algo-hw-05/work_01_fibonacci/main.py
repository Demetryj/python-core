"""Closure-based Fibonacci with caching"""

from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """Return a Fibonacci function that reuses computed values."""
    cache = {}  
    
    def fibonacci(n: int) -> int:
        """Compute Fibonacci number with memoization."""
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    
    return fibonacci

# def caching_fibonacci() -> Callable[[int], int]:
#     """Return a Fibonacci function that reuses computed values."""
#     cache: dict[int, int] = {0: 0, 1: 1} # Memoized results by n.

#     def fibonacci(n: int) -> int:
#         """Compute Fibonacci number with memoization."""
#         if n in cache:
#             return cache[n]
#         cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return cache[n]

#     return fibonacci
            

def main():
    fib = caching_fibonacci()
    print(fib(10))  
    print(fib(15))  
   

if __name__ == "__main__":
    main()
