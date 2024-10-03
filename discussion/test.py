empty = 'empty'
def is_link(s):
	return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
	assert is_link(rest), "rest must be a linked list."
	return [first, rest]

def first(s):
	assert is_link(s), "first only applies to linked lists."
	assert s != empty, "empty linked list has no first element."
	return s[0]

def rest(s):
	assert is_link(s), "rest only applies to linked lists."
	assert s != empty, "empty linked list has no rest."
	return s[1]

def len_link(s):
	length = 0
	while s != empty:
		s, length = rest(s), length + 1
	return length

def getitem_link(s, i):
	while i > 0:
		s, i = rest(s), i - 1
	return first(s)


def keep_if_link(f, s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept

four = link(1, link(2, link(3, link(4, empty))))
keep_if_link(lambda x: x%2 == 0, four)