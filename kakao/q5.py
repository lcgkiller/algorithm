def solution(str1, str2):
    str1 = " ".join(str1.upper().split(" "))
    str2 = " ".join(str2.upper().split(" "))
    if str1 == str2:
        return 1 * 65536

    else:
        perms1 = []
        perms2 = []

        for i in range(0, len(str1)-1):
            perms1.append(str1[i] + str1[i+1])

        for j in range(0, len(str2)-1):
            perms2.append(str2[j] + str2[j+1])

        print("perms1 : ", perms1)
        print("perms2 : ", perms2)

        perms1 = [x for x in perms1 if x.isalpha()]
        perms2 = [y for y in perms2 if y.isalpha()]

        if len(perms1) == 0 and len(perms2) == 0:
            return 1 * 65536

        elif set(perms1) == set(perms2):
            answer = int(len(perms1) / len(perms2) * 65536)
            return answer

        else:
            answer = int(len(set(perms1).intersection(perms2)) / len(set(perms1).union(perms2)) * 65536)
            return answer

        print("교집합 : ", set(perms1).intersection(perms2))
        print("합집합 : ", set(perms1).union(perms2))

    return answer

# print(solution("France", "french"))
# print(solution("handshake", "shake hands"))
# print(solution("ab+", "ab+"))
# print(solution("aa1+aa2", "AAAA12"))
# print(solution("E=M*C^2", "e=m*c^2"))
print(solution("1", "2"))


