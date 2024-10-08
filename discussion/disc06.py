def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

def differences(t):
    """Yield the differences between adjacent values from iterator t.
    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    first_num = next(t)
    while True:
        try:
            second_num = next(t)
        except StopIteration:
            break
        yield second_num - first_num
        first_num = second_num
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.
    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        for p in partition_gen(n - m, m):
            yield p + ' + ' + str(m)
    if m > 1:
        yield from partition_gen(n, m-1)