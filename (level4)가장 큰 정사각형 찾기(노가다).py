import time

def findLargestSquare(board):
    # board의 길이를 측정한다. 다만, 전역변수 max_x와 max_y를 좌표값으로 활용해야 하기 때문에 (실제 길이 - 1)을 한다.
    max_x = len(board) - 1
    max_y = len(board[0]) - 1

    max_square = 0 # 정사각형의 최대 넓이
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            for index in range(max_x, -1, -1):
                # (x + index와 y + index)는 대각선 방향으로 최대한 뻗을 수 있는 좌표값이다.
                # 전역변수 max_x와 max_y를 활용했다. 이 (max_x, max_y) 범위를 벗어나지 않아야 'O'의 개수를 셀 수 있다.
                if x + index <= max_x and y + index <= max_y:
                    count_o = 0 # 'O'의 개수를 세는 지역변수

                    # m, n은 5시 방향으로 뻗어나가는 대각선의 좌표값이다.
                    for m in range(x + index, x-1, -1):
                        for n in range(y + index, y-1, -1):
                            # 하나씩 m과 n을 줄여나가면서 개수를 센다.
                            if board[m][n] == "O":
                                count_o += 1

                                # 면적을 구하는데, index로 구했다. 면적값을 뭘로 구하던 상관은 없다.
                                # 대신, (면적 값) == (원의 개수)이고, max_square보다 크다면 최대 면적 넓이가 변경된다.
                                if (index+1)**2 == count_o:
                                    if max_square < count_o:
                                        max_square = count_o
                                    else:
                                        continue
    print("max_suqare : ", max_square)
    return max_square

# 아래 코드는 출력을 위한 테스트 코드입니다.

testBoard1 = [['X','O','O','O','X'],
              ['X','O','O','O','O'],
              ['X','X','O','X','O'],
              ['X','X','O','O','O'],
              ['X','X','X','X','X']]
#
testBoard2 = [['O', 'X', 'O', 'X', 'O'],
              ['X', 'O', 'O', 'X', 'O'],
              ['X', 'X', 'O', 'O', 'O'],
              ['X', 'O', 'O', 'O', 'X'],
              ['X', 'O', 'O', 'O', 'X']]

testBoard3 = [['O', 'X', 'O'],
              ['X', 'O', 'O'],
              ['X', 'O', 'O']]

testBoard4 = [['O', 'O', 'O'],
              ['O', 'O', 'O'],
              ['O', 'O', 'O']]


testBoard5 = [['X','O','O','O'],
              ['X','O','O','O'],
              ['X','X','O','O'],
              ['X','X','O','O']]

testBoard6 = [['X','O','O','O','O'],
              ['X','O','O','O','O'],
              ['X','O','O','O','O'],
              ['X','O','O','O','O'],
              ['X','O','O','O','O']]

testBoard7 = [['X','O','O','O','O', 'X'],
              ['X','O','O','O','O', 'X']]

print("board 1 : " ,findLargestSquare(testBoard1))

print("board 2 : " ,findLargestSquare(testBoard2))
print("board 3 : " ,findLargestSquare(testBoard3))
print("board 4 : " ,findLargestSquare(testBoard4))
print("board 5 : " ,findLargestSquare(testBoard5))
print("board 6 : " ,findLargestSquare(testBoard6))
print("board 7 : " ,findLargestSquare(testBoard7))
