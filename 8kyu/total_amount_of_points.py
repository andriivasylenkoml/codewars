def points(games):
    points = None
    for m in games:
        m = m.split(':')
        if m[0] > m[1]: points += 3
        if m[0] < m[1]: points += 0
        if m[0] == m[1]: points += 1
    return points