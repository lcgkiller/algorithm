def expressions(num):
    answer = 1
    origin_num = num
    _sum = 0
    pivot = num // 2 + 1


    for i in range(pivot, 0, -1):
        if _sum < origin_num:
            print("더해지는 값 : ", i)
            _sum += i
            print("합 출력 : ", _sum)

            if _sum > origin_num:
                continue

            elif _sum == origin_num:
                print("num : " , num)
                print("15? : ", _sum)
                answer += 1
                _sum = 0

    print("===answer===")
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(expressions(14))
print(expressions(15))
