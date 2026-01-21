#!/user/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a_first = 0
    else:
        a_first = tuple_a[0]
    if len(tuple_a) < 2:
        a_second = 0
    else:
        a_second = tuple_a[1]
    if len(tuple_b) == 0:
        b_first = 0
    else:
        b_first = tuple_b[0]
    if len(tuple_b) < 2:
        b_second = 0
    else:
        b_second = tuple_b[1]

    return (a_first + b_first, a_second + b_second)