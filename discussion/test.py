from disc05 import *
t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
print(has_path(t2, [5, 6]))