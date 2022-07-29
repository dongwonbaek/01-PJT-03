import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for _ in range(1, T + 1):
    test_case = list(map(int, input().split()))
    holsu = 0
    jjaksu = 0
    for a in range(1, len(test_case) + 1):
        if a % 2 == 1:
            holsu += test_case[a - 1] * 2
        else:
            jjaksu += test_case[a - 1]
    N = 10 - ((holsu + jjaksu) % 10)
    if N == 10:
        N = 0
    print(f'#{_} {N}')