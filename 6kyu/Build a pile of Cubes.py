def find_nb(m):
    total = 0
    n = 1

    while(total <= m):
        total += n**3
        if total == m: return n
        n += 1
    return -1