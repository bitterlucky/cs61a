class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def strange_loop():
    """
    >>> s= strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(1, Link(Link(1)))
    s.rest.first.rest = s
    return s
def sum_rec(s):
    """
    Returns the sum of the elements in s.
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_rec(a)
    14
    >>> sum_rec(Link.empty)
    0
    """
    # Use a recursive call to sum_rec
    if s == Link.empty:
        return 0
    elif type(s.first) == int:
        return s.first + sum_rec(s.rest) 
    else:
        return sum_rec(s.first) + sum_rec(s.rest)


def sum_iter(s):
    """
    Returns the sum of the elements in s.
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_iter(a)
    14
    >>> sum_iter(Link.empty)
    0
    """
    # Don't call sum_rec or sum_iter
    total = 0
    temp = s
    while temp is not Link.empty:
        total += temp.first
        temp = temp.rest
    return total

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.
    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b) # 3 and 7
    2
    >>> overlap(a.rest, b) # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    if s is Link.empty or t is Link.empty:
        return 0
    elif s.first == t.first:
        return 1 + overlap(s.rest, t.rest)
    elif s.first > t.first:
        return overlap(s, t.rest)
    else:
        return overlap(s.rest, t)