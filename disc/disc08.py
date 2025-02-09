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
    """Return a Link s for which s.rest.first.rest is s.
    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(6, Link(Link(1)))
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
    else:
        return s.first + sum_rec(s.rest)

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
    val = 0
    temp = s
    while temp != Link.empty:
        val += temp.first
        temp = temp.rest
    return val

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
    # if s is Link.empty or t is Link.empty:
    #     return 0
    # if s.first == t.first:
    #     return 1 + overlap(s.rest, t.rest)
    # elif s.first < t.first:
    #     return overlap(s.rest, t)
    # elif s.first > t.first:
    #     return overlap(s, t.rest)
    k = 0
    while s is not Link.empty and t is not Link.empty:
        if s.first == t.first:
            k += 1
            s = s.rest
            t = t.rest
        elif s.first < t.first:
            s = s.rest
        elif s.first > t.first:
            t = t.rest
    return k
        

def length(s):
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)
def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        frest = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, frest)
        else:
            return frest
def contained_in(s):
    def f(s, x):
        if s is Link.empty:
            return False
        else:
            return s.first == x or f(s.rest, x)
    return lambda x: f(s, x)
def overlap(s, t):
    """For s and t with no repeats, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8, Link(12))))))
    >>> overlap(a, b) # 3 and 7
    2
    >>> overlap(a.rest, b.rest) # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    return length(filter_link(contained_in(t), s))
