def high_and_low(numbers):
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    return str(max(numbers)) + " " + str(min(numbers))