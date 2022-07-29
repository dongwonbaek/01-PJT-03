import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for _ in range(1, T + 1):
    test_case = int(input())
    number_list = list(map(int, input().split()))
    result_list = []
    num_ = sum(number_list) / len(number_list)
    for A in number_list:
        if A <= num_:
            result_list.append(A)
    print(f'#{_} {len(result_list)}')