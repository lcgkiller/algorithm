def chooseCity(n,city):
    city.sort()
    print(city)
    result = city[0][0]
    left, right = 0, sum([city[i][1] for i in range(n)])
    for i in range(n-1):
        left += city[i][1]
        right -= city[i][1]
        print(left, right)
        if right > left:
            result = city[i+1][0]
    return result

#아래 코드는 출력을 위한 테스트 코드입니다.

'''풀이 외
def chooseCity(n, city):
    arr = [list(i) for i in zip(*city)]
    efficient_list = [0] * n
    for i in range(0, n):
        efficient_list[i] = sum(list(map(lambda a, b: abs(a - arr[0][i]) * b, arr[0][:i] + arr[0][i + 1:], arr[1][:i] + arr[1][i + 1:])))
    return city[efficient_list.index(min(efficient_list))][0]

#아래 코드는 출력을 위한 테스트 코드입니다.
print(chooseCity(3, [[1, 5], [2, 2], [3, 3]]))
'''
print(chooseCity(4, [[1, 5], [2, 2], [3, 29], [-1, 20]]))
# print(chooseCity(4,[[1,10],[2,2],[3,3], [-1,20]]))