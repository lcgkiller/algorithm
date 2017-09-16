def solution(n, arr1, arr2):
    answer = []
    matrix = []
    matrix.extend((arr1, arr2))
    result = []
    print(bin(5 & 8))
    for i, j in zip(*matrix):
        str_bin = bin(i | j)[2:]
        if len(str_bin) != n: # 길이가 n이 아니면 0을 채워줘야 한다.
            result.append(str_bin.zfill(n)) # string.zfill(width)

        else:
            result.append(bin(i | j)[2:]) # bin(i) 했을 때 출력결과는 0b001100 이런 형식으로 나오기 때문에 2번째부터 출력을 유

    for array in result:
        res = ""
        for j in array:
            res += "#" if j == "1" else " "
        answer.append(res)
    return answer


# print(solution(n=5, arr1=[9,20,28,18,11], arr2=[30,1,21,17,28]))
print(solution(n=6, arr1=[46, 33, 33 ,22, 31, 0], arr2=[27 ,56, 19, 14, 14, 0]))
# print(solution(n=7, arr1=[46, 33, 33 ,22, 31, 50, 31], arr2=[27,56, 19, 14, 14, 10, 31]))

