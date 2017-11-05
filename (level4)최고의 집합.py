def bestSet(n, s):
    if n > s:
        return [-1]

    else:
        element = s // n
        answer = [element] * n
        if sum(answer) != s:
            diff = s - sum(answer)
            for i in range(1, diff+1):
                answer[-i] += 1
            return answer

    return answer



# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(bestSet(3,13))
print(bestSet(9,80))