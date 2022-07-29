import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for _ in range(1, T + 1):
    test_case = list(map(int, input().split()))
    set_ = list(set(test_case))
    if len(set_) == 1:
        print(f'#{_} {set_[0]}')
    else:
        for a in test_case:
            if test_case.count(a) == 1:
                print(f'#{_} {a}')
                break