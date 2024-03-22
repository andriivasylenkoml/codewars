def find_smallest_A_length(P, Q, R):
    # Находим пересечение отрезков P и R
    intersection_PR = (max(P[0], R[0]), min(P[1], R[1]))

    # Если пересечение не пусто, то A будет отрезком Q, который не пересекается с этим пересечением
    if intersection_PR[0] <= intersection_PR[1]:
        A_length = Q[1] - Q[0]
    else:
        # Если пересечение пусто, то A будет отрезком, который не содержит ни одной точки из P и R
        A_length = max(Q[1] - P[1], R[0] - Q[0])

    return A_length

# Определение отрезков P, Q и R
P = [1023, 2148]
Q = [1362, 3898]
R = [1813, 2566]

# Находим наименьшую возможную длину отрезка A
smallest_A_length = find_smallest_A_length(P, Q, R)

print("Наименьшая возможная длина отрезка A:", smallest_A_length)
