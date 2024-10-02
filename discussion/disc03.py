def swipe(n):
    """Print the digits of n, one per line, first backward then forward.
    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...
    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1:
        return n
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def f(i):
        if n == i:
            return True
        elif n % i == 0:
            return False
        else:
            return f(i + 1)
    return f(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n,
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    if n == 1:
        print(1)
        return 1
    elif n % 2 == 0:
        print(n)
        return 1 + hailstone(n // 2)
    else:
        print(n)
        return 1 + hailstone(3 * n  + 1)

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.
    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def helper(current_number, player, direction):
        if current_number == n:
            return player
        if has_seven(current_number):
            if player - direction == 0:
                return helper(current_number + 1, k, -1 * direction)
            elif player - direction == k + 1:
                return helper(current_number + 1, 1, -1 * direction)
            else:
                return helper(current_number + 1, player - direction, -1 * direction)
        if player + direction == 0:
            return helper(current_number + 1, k, direction)
        elif player + direction == k + 1:
            return helper(current_number + 1, 1, direction)
        else:
            return helper(current_number + 1, player + direction, direction)
    return helper(1, 1, 1)

def has_seven(n):
    #n is bigger than 0
    if n % 7 == 0:
        return True
    if n < 10 and n != 7:
        return False
    while n > 0:
        if n % 10 == 7:
            return True
        n = n // 10
    return False
