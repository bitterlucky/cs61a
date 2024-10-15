def fit(total, n):
    def inner(total, n, x):
        if n == 0 and total == 0:
            return True
        elif total == 0 and n != 0:
            return False
        elif total != 0 and n == 0:
            return False
        elif x * x > total:
            return False
        else:
            return inner(total - x * x, n - 1, x + 1) or inner(total, n, x + 1)
    return inner(total, n, 1)