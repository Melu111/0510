def arif(*numbers):
    if len(numbers) == 0:
        return 0
    s = 0
    for x in numbers:
        s = s + x
    return s / len(numbers)

print(arif(2, 5, 6, 2, 4, 8, 12))