def chooseCity(n,city):
    answer = 0
    _list = []
    dist = []
    for j in range(0, n):
        dist.append(city[j][0])

    for i in (0, n):
        _list.append(city[:i] + city[i+1:])
    print(_list)

    # return answer

#아래 코드는 출력을 위한 테스트 코드입니다.

print(chooseCity(3,[[1,5],[2,2],[3,3]]))