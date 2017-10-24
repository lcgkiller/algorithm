def expressions(num):
    print([i for i in range(1, num+1, 2) if num % i is 0])
    return len([i for i in range(1,num+1,2) if num % i is 0])


# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(expressions(1))
print(expressions(15))
# print(expressions(9598))
