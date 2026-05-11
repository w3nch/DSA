import random
import time

def generate_matrix(n):
    """Generate n x n matrix with random integers."""
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

def matrix_multiply(a, b):
    """Multiply two matrices."""
    n = len(a)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result

def fibonacci(n, memo={}):
    """Recursive Fibonacci with memoization."""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def sort_large_list(size):
    """Generate a large list and sort it."""
    lst = [random.randint(0, 1000000) for _ in range(size)]
    lst.sort()
    return lst

def string_processing(n):
    """Generate random strings and count vowels."""
    vowels = "aeiou"
    count = 0
    for _ in range(n):
        s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=50))
        count += sum(1 for c in s if c in vowels)
    return count

if __name__ == "__main__":
    start = time.time()

    print("Generating matrices...")
    mat1 = generate_matrix(100)
    mat2 = generate_matrix(100)
    print("Multiplying matrices...")
    _ = matrix_multiply(mat1, mat2)

    print("Computing Fibonacci(30)...")
    fib = fibonacci(30)

    print("Sorting large list...")
    sorted_list = sort_large_list(50000)

    print("Processing strings...")
    vowels_count = string_processing(20000)

    end = time.time()
    print(f"Fibonacci(30) = {fib}")
    print(f"Total vowels counted = {vowels_count}")
    print(f"Execution time: {end - start:.2f} seconds")
