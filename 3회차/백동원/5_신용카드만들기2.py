from re import A
import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for _ in range(1, T + 1):
    number = input().split()
    test_case = []
    for a in number[0]:
        test_case.append(a)
    if (len(test_case) - test_case.count('-') == 16) and (test_case[0] in '34569'):
        print(f'#{_} 1')
    else:
        print(f'#{_} 0')