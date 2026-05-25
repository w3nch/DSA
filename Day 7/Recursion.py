print("Tell me the number: ")
user_input = int(input())


### Without recursion
def factorial(n: int) -> int:
    fact = 1
    try:
        for i in range(1, n + 1):
            fact = i * fact
    except ValueError:
        print("input type should be int")
    return fact


# print(factorial(4))
# print(factorial(4))


### Recursion
def recursion_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1

    return n * recursion_factorial(n - 1)


print(recursion_factorial(user_input))
