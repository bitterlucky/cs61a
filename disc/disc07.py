def draw(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed( [hand.pop(i) for i in reversed(sorted(positions))] ))

class Eye:
    """An eye.
    >>> Eye().draw()
    '•'
    >>> print(Eye(False).draw(), Eye(True).draw())
    • -
    """
    def __init__(self, closed = False):
        self.closed = closed
    def draw(self):
        if self.closed:
            return '-'
        else:
            return '•'
    
