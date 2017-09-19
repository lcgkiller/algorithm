def solution(n, arr1, arr2):

    print([format((x | y), '0%db' % 3) for x, y in zip(arr1, arr2)])

    # return [format((x | y), '0%db' % n).replace('0', ' ').replace('1', '#') for x, y in zip(arr1, arr2)]



print(solution(n=6, arr1=[46, 33, 33, 22, 31, 0], arr2=[27, 56, 19, 14, 14, 0]))