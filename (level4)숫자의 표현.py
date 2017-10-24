def expressions(num):
    answer = 1 # 모든 num은 자기 자신을 답으로 가진다.
    _sum = 0
    left = 0

    while left != (num // 2 + 1): # left
        if _sum < num:
            for right in range(left+1, num // 2 + 1 + 1):
                _sum += right
                print("left : ", left, "right : ", right, "sum : ", _sum)

                if _sum == num:
                    answer += 1
                    left += 1
                    _sum = 0
                    break

                elif _sum > num:
                    left += 1
                    _sum = 0
                    break

    print("=====answer=====")
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(expressions(15))
