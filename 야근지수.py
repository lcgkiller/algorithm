def noOvertime(n, works):
    result = 0
    # 야근 지수를 최소화 하였을 때의 야근 지수는 몇일까요?
        # 1. 우선 max value를 찾아서 두 번째 max value보다 낮추는게 중요하다.

    while n != 0:
        max_value = max(works)
        max_index = works.index(max_value)
        works[max_index] -= 1
        n -= 1

    for i in range(0, len(works)):
        result += works[i] ** 2

    return result


print(noOvertime(4, [4, 3, 3]))
