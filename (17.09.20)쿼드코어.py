# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
# - 입력과 출력은 input()과 print()를 사용하세요

def answer_find(cost):
    print(cost)


# 가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
    # <---메인 코드의 시작--->

    # 테스트케이스의 수를 입력받는다
    answer = 0  # 정답을 이 변수에 저장한다

    # 5개의 작업에 대한 소요 시간을 입력받는다
    cost = [int(ts) for ts in input().split()]

