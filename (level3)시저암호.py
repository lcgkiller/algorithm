def caesar(s, n):
    n = n % 26
    caesar_list = []

    for char in range(0, len(s)):

        caesar = chr(ord(s[char]) + n)

        if s[char] == " ":
            caesar_list.append(" ")
            continue

        if s[char].isupper():
            if caesar > chr(ord("Z")):
                caesar = chr(ord("A") + (ord(s[char]) + n - ord("A")) - 26)
        else:
            if caesar > chr(ord("z")):
                caesar = chr(ord("a") + (ord(s[char]) + n - ord("a")) - 26)

        caesar_list.append(caesar)
    result = "".join(caesar_list)
    return result

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
