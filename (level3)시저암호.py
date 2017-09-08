def caesar(s, n):
    n = n % 26
    caesar_list = []

    for char in range(0, len(s)):

        caesar = chr(ord(s[char]) + n)

        if s[char] == " ": # 공백 처리
            caesar_list.append(" ")
            continue

        if s[char].isupper(): # 대문자 처리
            if caesar > chr(ord("Z")):
                caesar = chr((ord(s[char]) + n - 26))
        else: # 소문자 처리
            if caesar > chr(ord("z")):
                caesar = chr((ord(s[char]) + n - 26))

        caesar_list.append(caesar)
    result = "".join(caesar_list) # 리스트를 문자열로 만들어줌
    return result

# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))


