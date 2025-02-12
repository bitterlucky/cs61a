def enumerate(s):
    def inner(s, n):
        if len(s) == 0:
            return []
        else:
            lst = [[n, s[0]]]
            lst.extend(inner(s[1:], n + 1))
            return lst
    return inner(s, 0)
print(enumerate([3,4,5,6]))