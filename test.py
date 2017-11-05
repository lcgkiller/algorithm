def hopscotch(board, size):
    accum = [0] * len(board[0])

    for row in board:
        tmp = accum[:]
        for i in range(len(row)):
            tmp1 = tmp[:i]
            tmp2 = tmp[i+1:]
            accum[i] = row[i] + max(tmp[:i] + tmp[i+1:])

    return max(accum)

#아래는 테스트로 출력해 보기 위한 코드입니다.
# board =  [[ 1, 2, 3, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
board =  [[ 1, 2, 5, 5 ], [ 5, 6, 7, 8 ], [4, 3, 2, 1]]
print(hopscotch(board, 3))
