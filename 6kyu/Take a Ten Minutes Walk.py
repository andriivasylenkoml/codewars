def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') != walk.count('s'):
        return False
    if walk.count('w') != walk.count('e'):
        return False
    return True