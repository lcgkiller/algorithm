# map을 이용한 풀이

def func():
    a, b = map(int, input().split())
    if 0<a<10 and 0<b<10:
        return print(a + b)
    else:
        return 0

func()