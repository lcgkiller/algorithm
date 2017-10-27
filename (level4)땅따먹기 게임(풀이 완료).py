def hopscotch(board, size):
    result = max(board[0])
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for row in range(1, size):
        pre_max = max(board[row-1])
        cur_max = max(board[row])
        pre_max_idx = board[row - 1].index(max(board[row - 1]))
        cur_max_idx = board[row].index(max(board[row]))
        cmp_diff = (max(board[row - 1]) - sorted(board[row - 1])[-2]) < (max(board[row]) - sorted(board[row])[-2])
        pre_is_dup = True if max(board[row - 1]) in board[row - 1][pre_max_idx + 1:] else False
        cur_is_dup = True if max(board[row    ]) in board[row    ][cur_max_idx + 1:] else False

        if pre_is_dup and cur_is_dup:
            result += cur_max
        elif pre_is_dup and not cur_is_dup:
            result += cur_max
        elif not pre_is_dup and cur_is_dup:
            result += cur_max
        elif not pre_is_dup and not cur_is_dup:
            if pre_max_idx != cur_max_idx:
                result += cur_max
            elif pre_max_idx == cur_max_idx:
                if cmp_diff:
                    result = result - pre_max + sorted(board[row-1])[-2] + cur_max
                else:
                    result += sorted(board[row])[-2]
    return result


#아래는 테스트로 출력해 보기 위한 코드입니다.
board  =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
board2 =  [[ 1, 2, 5, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
board3 = [[1, 9, 9, 9], [9, 10, 9, 8], [6, 4, 5, 1], [4, 9, 6, 5], [10, 4, 3, 10], [8, 8, 6, 5], [3, 9, 6, 7], [3, 8, 4, 3], [6, 4, 4, 6], [5, 7, 7, 10]]
board4 = [[9, 7, 10, 2], [3, 7, 3, 7], [5, 4, 7, 4], [8, 7, 9, 10], [8, 1, 7, 5], [3, 6, 8, 4], [3, 9, 8, 8], [4, 10, 2, 3], [5, 2, 4, 5], [2, 8, 6, 8]]
board5 = [[6, 10, 8, 6], [6, 8, 9, 4], [9, 1, 3, 1], [8, 2, 1, 2], [1, 4, 7, 5], [1, 2, 6, 10], [3, 1, 4, 9], [2, 4, 6, 3], [9, 10, 6, 5], [9, 4, 3, 7]]
board6 = [[6, 12, 12, 6], [8, 9, 9, 8]]
# print(hopscotch(board, 3))
# print(hopscotch(board2, 3))
# print(hopscotch(board3, 10))
print(hopscotch(board4, 10))
print(hopscotch(board5, 10))
print(hopscotch(board6, 2))

