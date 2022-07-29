import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for _ in range(T):
    test_case = int(input())
    score_amnt = []
    index_list = []
    score_list = list(map(int, input().split()))
    score_kind = list(set(score_list))
    for A in score_kind:
        score_amnt.append(score_list.count(A))
    for B in range(len(score_amnt)):
        if score_amnt[B] == max(score_amnt):
            index_list.append(score_kind[B])
    print(f'#{test_case} {max(index_list)}')