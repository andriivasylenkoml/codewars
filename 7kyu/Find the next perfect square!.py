def find_next_square(sq):
    root = sq ** 0.5
    return (root + 1) ** 2 if root.is_integer() == True else -1