def noOvertime(n, works):
    result = 0

    while n != 0:
        max_value = max(works)
        max_index = works.index(max_value)
        works[max_index] -= 1
        n -= 1

    for i in range(0, len(works)):
        result += works[i] ** 2

    return result


print(noOvertime(4, [4, 3, 3]))
