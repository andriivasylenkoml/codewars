def delete_nth(order,max_e):
    result = []
    counts = {}
    for num in order:
        if num not in counts:
            counts[num] = 1
            result.append(num)
        elif counts[num] < max_e:
            counts[num] += 1
            result.append(num)
    return result