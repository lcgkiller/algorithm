import collections

def findLargestSquare(board):
    new_list = []
    len_board = len(board)
    _max = 0

    for row in board:
        print(row)

    # 'O'의 개수가 board의 길이의 제곱과 같다면 가장 큰 정사각형의 넓이를 반환한다.
    if len_board ** 2 == [element for sub_list in board for element in sub_list].count('O'):
        return len_board ** 2

    else:
        for i in range(0, len(board) // 2 + 1):
            indices = [i for i, row in enumerate(list(board[i])) if row == "O"] # 출력결과 : [0], [1,2], [1,2]와 같이 'O'가 있는 부분을 인덱스 값으로 출력해줌

            count_len = 0
            max_len = 0
            for index in range(0, len(indices) -1):
                if indices[index] + 1 == indices[index + 1]:
                    count_len += 1
                    max_len = count_len + 1
                else:
                    count_len = 0

            # indices의 길이(리스트)가 1이면 최대 넓이는 1이므로 건너뛰어도 됨.
            if max_len >= 2:
                print(indices)
                # print("{}번째 리스트 : {}".format(i, indices))
                for k in indices:
                    print("{}번째 행 {}번째 열 ".format(i, k))
            # for j in range(0, len(board[i]) // 2 + 1):
            #     print(j)


        # for row in board:
        #     print(row)
        #     indices = [i for i, row in enumerate(list(row)) if row == "O"]
        #     print(indices)
            # for index in range(0, len(row)):
            #     print(row[index])

    print("===================")


    # for row in board:
    #     indices = [i for i, row in enumerate(list(row)) if row == "O" ]
    #     new_list.append(indices)
    #
    # print(new_list)
    #
    # for sub_list in new_list:
    #     count_len = 0
    #     max_len = 0
    #     for index in range(0, len(sub_list) -1 ):
    #         if sub_list[index] + 1 == sub_list[index + 1]:
    #             count_len += 1
    #             max_len = count_len + 1
    #         else:
    #             count_len = 0
    #
    #     print("최대길이 : ", max_len)

    # for i in new_list:
    #     count_len = 0
    #     for j in i:
    #         if j == '':
    #             count_len = 0
    #             continue
    #         else:
    #             count_len += 1
    #
    #     print(count_len)



    # print("==============zip(*board)===============")
    #
    # for row in zip(*board):
    #     indices = [i if row == "O" else '' for i, row in enumerate(list(row))]
    #     zip_list.append(indices)
    #
    # for i in zip_list:
    #     print(i)

    # for i in range(0, len(new_list)):
    #     print("서브리스트 : ", new_list[i])
    #     print("길이 :", len(new_list[i]))

        # for j in range(0, len(new_list[i])):
        #     print(new_list[i][j])
            # if new_list[i][j] is not '':  # none은 건너뛴다.
            #     print("{}행".format(i), "{}열 :".format(j), "값 :", new_list[i][j])
                # print(len(new_list[i]))
                # for sub_list in new_list:
                #     for element in sub_list:
                #         if element is '':
                #             continue
                #         else:
                #             print(element)
                #
                # print("================================")
                # new_list = []
                #
                #
                # for row in board:
                #     indices = [i if row == "O" else '' for i, row in enumerate(list(row))]
                #     indices = [i for i, row in enumerate(list(row))]
                # print(new_list.append(indices))

                # print("================================")
                # print(new_list)
                # for index in range(0, len(new_list) - 1):
                #     print(new_list[index])
                #     for element in new_list[index]:
                #         if element is not '':
                #             print(element)

                # print("================================")
                #
                # for char in zip(*new_list):
                #     print(list(char))

                # return answer


# 아래 코드는 출력을 위한 테스트 코드입니다.

testBoard = [['X','O','O','O','X'],
             ['X','O','O','O','O'],
             ['X','X','O','O','O'],
             ['X','X','O','O','O'],
             ['X','X','X','X','X']]
# testBoard2 = [['O', 'X', 'O', 'X', 'O'],
#              ['X', 'O', 'O', 'X', 'O'],
#              ['X', 'X', 'O', 'O', 'O'],
#              ['X', 'O', 'O', 'O', 'X'],
#              ['X', 'O', 'O', 'O', 'X']]
testBoard3 = [['O', 'X', 'O'],
              ['X', 'O', 'O'],
              ['X', 'O', 'O']]
# testBoard4 = [['O', 'O', 'O'],
#               ['O', 'O', 'O'],
#               ['O', 'O', 'O']]
print(findLargestSquare(testBoard))
# print(findLargestSquare(testBoard2))
print(findLargestSquare(testBoard3))
# print(findLargestSquare(testBoard4))
