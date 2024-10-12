def square(x):
    return x * x
def compose(f, g):
    def inner(x):
        return f(g(x))
    return inner
def repeat(f, n):
    def inner(x):
        if n == 0:
            return x
        else:
            return repeat(f, n - 1)(f(x))
    return inner