# 1. Factorial


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# 2. Sum of Numbers from 1 to n


def sum_numbers(n: int) -> int:
    if n == 1:
        return 1

    return n + sum_numbers(n - 1)


print(sum_numbers(5))


# 3. Power Function


def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1

    return base * power(base, exp - 1)


print(power(2, 3))


# 4. Fibonacci Number


def fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# 5. Countdown Recursively


def countdown(n: int) -> None:
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)


# 6. Reverse a String


def reverse_string(text: str) -> str:
    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]


print(reverse_string("hello"))


# 7. Sum of Digits


def sum_digits(n: int) -> int:
    if n == 0:
        return 0

    return n % 10 + sum_digits(n // 10)


print(sum_digits(1234))


# 8. Check Palindrome


def is_palindrome(text: str) -> bool:
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


print(is_palindrome("madam"))


# 9. Multiply Using Recursion Only


def multiply(a: int, b: int) -> int:
    if b == 0:
        return 0

    return a + multiply(a, b - 1)


print(multiply(4, 3))
