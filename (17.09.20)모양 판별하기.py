# -*- coding: utf-8 -*-
# 한국어 주석을 사용할 경우 UTF-8 encoding을 꼭 이용해주세요

# [Notice for Python3]
# - 별도의 병렬 처리나 시스템콜, 네트워크/파일접근 등을 하지 마세요
# - 기본 제공되는 뼈대 코드는 입출력의 이해를 돕기위해 제공되었습니다.
# - 뼈대코드의 활용은 선택사항이며 코드를 직접 작성하여도 무관합니다.

def answer(px, py, qx, qy):

    if px == py == qx == qy:
        return print("DOT")

    elif (px == qx and py != qy ) or (py == qy and qx == qy):
        return print("SEGMENT")

    else:
        abs_x = abs(qx - px)
        abs_y = abs(qy - py)
        abs_xy = abs(px - qy)
        abs_yx = abs(py - qx)

        if abs_x == abs_y == abs_xy == abs_yx:
            return print("SQUARE")

        else:
            return print("RECTANGLE")


# 가장 먼저 실행되는 메인 코드
if __name__ == "__main__":
    # <---메인 코드의 시작--->

    # 첫 번째 점 p의 좌표
    px, py = list(map(int, input().split()))

    # 두 번째 점 q의 좌표
    qx, qy = list(map(int, input().split()))

    answer(px, py, qx, qy)

    # <---메인 코드의 끝--->
