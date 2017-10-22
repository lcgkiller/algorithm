import time

def findLargestSquare(board):
    max_x = len(board) - 1
    max_y = len(board[0]) - 1
    print("max_x : ", max_x, "max_y : ", max_y)
    max_square = 0
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            for index in range(max_x, -1, -1):
                if x + index <= max_x and y + index <= max_y:
                    print(x+index, y+index)
                    count_o = 0

                    for m in range(x+index, x-1, -1):
                        for n in range(y+index, y-1, -1):
                            if board[m][n] == "O":
                                count_o += 1
                                print("O 개수 : ", count_o)
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
              ['X','X','O','O','O'],
              ['X','X','O','O','O']]

testBoard7 = [['X','O','O','O','O', 'X'],
              ['X','O','O','O','O', 'X']]

print("board 1 : " ,findLargestSquare(testBoard1))

print("board 2 : " ,findLargestSquare(testBoard2))
print("board 3 : " ,findLargestSquare(testBoard3))
print("board 4 : " ,findLargestSquare(testBoard4))
print("board 5 : " ,findLargestSquare(testBoard5))
print("board 6 : " ,findLargestSquare(testBoard6))
print("board 7 : " ,findLargestSquare(testBoard7))
