# number_utils.py

def is_prime(n: int) -> bool:
    """check if the number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False
    return True

def is_armstrong(n: int) -> bool:
    """check if  the number is Armstrong number."""
    s = str(abs(n))
    power = len(s)
    return sum(int(digit) ** power for digit in s) == abs(n)

def is_perfect(n: int) -> bool:
    """check if the number is perfect number"""
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
           sum_divisor += i
           if i != n // i:
               sum_divisors += n // i
    return sum_divisors == n

def digit_sum(n: int) -> int:
    """ Calcaulate the sum of the digits of the number."""
    return sum(int(d) for d in str(abs(n)))

def get_parity(n: int) -> str:
    """Determine if the number is 'even' or 'odd'."""
    return  "odd" if n % 2 != 0 else "even"

