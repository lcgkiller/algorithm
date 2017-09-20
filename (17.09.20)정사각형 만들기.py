



# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.
# - 입력과 출력은 input()과 print()를 사용하세요

def answer(num, coordinate):
    print(coordinate)
    list_coordinate = []
    for index in zip(*coordinate):
        list_coordinate += index

    x = list_coordinate[0:len(list_coordinate)//2]
    y = list_coordinate[len(list_coordinate)//2:]



#가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
	# <---메인 코드의 시작--->

    coordinate = []
    num = input()
    for _input in range(0, int(num)):
        coordinate += [list(map(int, input().split()))]


    answer(int(num), coordinate)
	# <---메인 코드의 끝--->
