def f(x):
    return x - 1
def g(x):
    return x * 2
def h(x, y):
    return int(str(x) + str(y))


print(h(g(g(5)), g(g(f(f(f(f(g(5)))))))))
