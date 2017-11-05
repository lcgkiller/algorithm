def bestSet(n, s):
    return [s//n] * (n-s % n) + [s//n + 1] * (s % n) if n<=s else [-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(bestSet(3,13))
print(bestSet(8,80))