# from scheme_reader import *
from scheme import *
expr = Pair("+", Pair(2, Pair(2, nil)))
scheme_eval(expr, create_global_frame())
