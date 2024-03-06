def points(games):
    points = 0
    for m in games:
        m = m.split(':')
        if m[0] > m[1]: points += 3
        if m[0] == m[1]: points += 1
    return points