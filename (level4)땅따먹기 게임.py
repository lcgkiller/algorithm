def hopscotch(board, size):
    result = max(board[0])
    print("합 : ", result)
    # 땅따먹기 게임으로 얻을 수 있는 최대 점수는?
    for row in range(1, size):
        pre_idx_max = board[row - 1].index(max(board[row - 1]))
        cur_idx_max = board[row].index(max(board[row]))
        cmp_diff = (max(board[row - 1]) - sorted(board[row - 1])[-2]) < (max(board[row]) - sorted(board[row])[-2])
        # 선 중복 검사!
        if max(board[row - 1]) in board[row - 1][pre_idx_max + 1:]:  # 중복값이 있는 경우
            for i in range(0, len(board[row - 1])):
                if pre_idx_max == i:
                    continue
                elif pre_idx_max != i and board[row - 1][i] == max(board[row - 1]):
                    # 전 줄에서 중복값이 있다면, 현재줄의 pre_idx_max의 값이 더 크다면 전 줄의 i(중복되는 인덱스)를 선택해야 한다.
                    if board[row][pre_idx_max] > board[row][i]:
                        result += board[row][pre_idx_max]
                        print("** row({})번째 줄 인덱스 ({}, {})에 max값이 중복된다. 따라서 다음 줄을 비교한다. **".format(row - 1,
                                                                                                   pre_idx_max, i,
                                                                                                   row))
                        print("** board[{}][{}] : {}, board[{}][{}] : {} **".format(row, pre_idx_max,
                                                                                    board[row][pre_idx_max], row, i,
                                                                                    board[row][i]))
                        print("더해지는 값 : ", board[row][pre_idx_max])
                        print("합 : ", result)

                        break
                    # 전 줄에 중복값이 있지만, 현재줄의 pre_idx_max값이 중복 max값의 인덱스인 i보다 작다면, 문제가 없다.
                    else:
                        result += max(board[row])
                        print("board[row][i] row({})번째 줄 : {}".format(row, max(board[row])))
                        print("더해지는 값 : ", max(board[row]))
                        print("합 : ", result)

                        break

        elif max(board[row - 1]) not in board[row - 1][pre_idx_max + 1:]: # 중복값이 없는 경우
            if pre_idx_max != cur_idx_max:
                result += max(board[row])
                print("더해지는 값 : ", max(board[row]))
                print("합 : ", result)

            elif pre_idx_max == cur_idx_max:
                # (중복값이 없으며) 전 줄과 현재 줄의 max idx가 위치가 서로 같으면, 피해가야 한다.
                # 단, {(전 줄의 가장 큰 값) - (전 줄의 두 번째로 큰 값)} < {(현재 줄의 가장 큰 값) - (현재 줄의 두 번쨰로 큰 값)}이면 문제가 된다.
                if cmp_diff:
                    # cmp_diff가 참이면 전 줄에서 가장 큰 값을 도로 빼주고, 전 줄의 두 번째로 큰 값 + 현재 줄의 가장 큰 값을 한다.
                    print("True : {}번째 줄 ".format(row))
                    result = (result - max(board[row-1]) + sorted(board[row-1])[-2]) + max(board[row])
                    print("전 줄의 max값 ", max(board[row-1]), "전 줄의 두 번째로 큰 값 : ", sorted(board[row-1])[-2], "더해야 하는 값 : ", max(board[row]))
                else:
                    result += sorted(board[row])[-2]
                    print("더해지는 값 : ", sorted(board[row])[-2])
                    print("합 : ", result)

    return result


#아래는 테스트로 출력해 보기 위한 코드입니다.

# board  =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
# board2 =  [[ 1, 2, 5, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
# board3 = [[1, 9, 9, 9], [9, 10, 9, 8], [6, 4, 5, 1], [4, 9, 6, 5], [10, 4, 3, 10], [8, 8, 6, 5], [3, 9, 6, 7], [3, 8, 4, 3], [6, 4, 4, 6], [5, 7, 7, 10]]
# board4 = [[9, 7, 10, 2], [3, 7, 3, 7], [5, 4, 7, 4], [8, 7, 9, 10], [8, 1, 7, 5], [3, 6, 8, 4], [3, 9, 8, 8], [4, 10, 2, 3], [5, 2, 4, 5], [2, 8, 6, 8]]
# board5 = [[6, 10, 8, 6], [6, 8, 9, 4], [9, 1, 3, 1], [8, 2, 1, 2], [1, 4, 7, 5], [1, 2, 6, 10], [3, 1, 4, 9], [2, 4, 6, 3], [9, 10, 6, 5], [9, 4, 3, 7]]
# print(hopscotch(board, 3))
# print(hopscotch(board2, 3))
# print(hopscotch(board3, 10))
# print(hopscotch(board4, 10))
# print(hopscotch(board5, 10))