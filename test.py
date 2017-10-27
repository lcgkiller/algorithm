def hopscotch(board, size):
    result = max(board[0])
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for row in range(1, size):
        pre_idx_max = board[row - 1].index(max(board[row - 1]))
        cur_idx_max = board[row].index(max(board[row]))
        cmp_diff = (max(board[row - 1]) - sorted(board[row - 1])[-2]) < (max(board[row]) - sorted(board[row])[-2])
        is_duplicated = True if max(board[row - 1]) in board[row - 1][pre_idx_max + 1:] else False

        if pre_idx_max != cur_idx_max:
            result += board[row][cur_idx_max]
        else:
            if is_duplicated:
                for i in range(0, len(board[row - 1])):
                    if pre_idx_max == i:
                        continue
                    elif pre_idx_max != i and board[row - 1][i] == max(board[row - 1]):
                        # 전 줄에서 중복값이 있다면, 현재줄의 pre_idx_max의 값이 더 크다면 전 줄의 i(중복되는 인덱스)를 선택해야 한다.
                        if board[row][pre_idx_max] > board[row][i]:
                            result += board[row][pre_idx_max]
                            break

            elif cmp_diff:
                result = result - max(board[row-1]) + sorted(board[row-1])[-2] + max(board[row])

            else:
                result += sorted(board[row])[-2]
    return result


#아래는 테스트로 출력해 보기 위한 코드입니다.
# board  =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
# board2 =  [[ 1, 2, 5, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
board3 = [[1, 9, 9, 9], [9, 10, 9, 8], [6, 4, 5, 1], [4, 9, 6, 5], [10, 4, 3, 10], [8, 8, 6, 5], [3, 9, 6, 7], [3, 8, 4, 3], [6, 4, 4, 6], [5, 7, 7, 10]]
# board4 = [[9, 7, 10, 2], [3, 7, 3, 7], [5, 4, 7, 4], [8, 7, 9, 10], [8, 1, 7, 5], [3, 6, 8, 4], [3, 9, 8, 8], [4, 10, 2, 3], [5, 2, 4, 5], [2, 8, 6, 8]]
# board5 = [[6, 10, 8, 6], [6, 8, 9, 4], [9, 1, 3, 1], [8, 2, 1, 2], [1, 4, 7, 5], [1, 2, 6, 10], [3, 1, 4, 9], [2, 4, 6, 3], [9, 10, 6, 5], [9, 4, 3, 7]]
board6 = [[6, 10, 12, 6], [4, 4, 9, 4]]
board7 = [[10, 6, 8, 9], [5, 4, 10, 10], [7, 4, 4, 3], [2, 1, 3, 3], [10, 3, 1, 2], [9, 5, 8, 6], [6, 8, 7, 7], [5, 1, 5, 8], [8, 6, 8, 9], [3, 2, 9, 7]]
# print(hopscotch(board, 3))
# print(hopscotch(board2, 3))
print(hopscotch(board3, 10))
# print(hopscotch(board4, 10))
# print(hopscotch(board5, 10))
print(hopscotch(board6, 2))
