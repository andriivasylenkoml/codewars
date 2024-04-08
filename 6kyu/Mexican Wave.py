def wave(people: str) -> list:
    result = []
    for index, man in enumerate(people):
        if man.isalpha():
            result.append(people[:index] + people[index].upper() + people[index + 1:])
    return result