def findLargestSquare(board):
    table = [[1 if x == "O" else 0 for x in sub_board] for sub_board in board]
    max_square = 0
    for x in range(1, len(table)):
        for y in range(1, len(table[x])):
            if table[x][y] == 0:
                continue
            # 해당 좌표 기준(x,y) : 왼쪽검사(x, y-1), 위쪽 검사(x-1, y), 11시 방향 대각선 검사(x-1, y-1)
            else:
                _min = min([table[x][y-1], table[x-1][y], table[x-1][y-1]])
                table[x][y] = _min + 1
                if max_square < table[x][y]:
                    max_square = table[x][y]

    return max_square**2

testBoard1 = [['X', 'O', 'O', 'O', 'X'],
              ['X', 'O', 'O', 'O', 'O'],
              ['X', 'X', 'O', 'X', 'O'],
              ['X', 'X', 'O', 'O', 'O'],
              ['X', 'X', 'X', 'X', 'X']]

# testBoard2 = [['O', 'X', 'O', 'X', 'O'],
#               ['X', 'O', 'O', 'X', 'O'],
#               ['X', 'X', 'O', 'O', 'O'],
#               ['X', 'O', 'O', 'O', 'X'],
#               ['X', 'O', 'O', 'O', 'X']]
#
# testBoard3 = [['O', 'X', 'O'],
#               ['X', 'O', 'O'],
#               ['X', 'O', 'O']]
#
testBoard4 = [['O', 'O', 'O'],
              ['O', 'O', 'O'],
              ['O', 'O', 'O']]
#
#
# testBoard5 = [['X','O','O','O'],
#               ['X','O','O','O'],
#               ['X','X','O','O'],
#               ['X','X','O','O']]
#
# testBoard6 = [['X','O','O','O','O'],
#               ['X','O','O','O','O'],
#               ['X','X','O','O','O'],
#               ['X','X','O','O','O']]
#
# testBoard7 = [['X','O','O','O','O', 'X'],
#               ['X','O','O','O','O', 'X']]

testBoard8 = [['X', 'O', 'X', 'O', 'X'],
              ['O', 'X', 'O', 'X', 'O'],
              ['X', 'O', 'X', 'O', 'X'],
              ['O', 'X', 'O', 'X', 'O'],
              ['X', 'O', 'X', 'O', 'X']]

print("board 1 : ", findLargestSquare(testBoard1))

# print("board 2 : " ,findLargestSquare(testBoard2))
# print("board 3 : " ,findLargestSquare(testBoard3))
# print("board 4 : " ,findLargestSquare(testBoard4))
# print("board 5 : " ,findLargestSquare(testBoard5))
# print("board 6 : " ,findLargestSquare(testBoard6))
# print("board 7 : " ,findLargestSquare(testBoard7))
print("board 7 : " ,findLargestSquare(testBoard8))

