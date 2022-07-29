import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for _ in range(1, T + 1):
    test_case = input()
    word_list = []
    for a in test_case[::-1]:
        word_list.append(a)
    # word = test_case[::-1]
    for a in range(len(word_list)):
        if word_list[a] == 'b':
            word_list[a] = 'd'
        elif word_list[a] == 'd':
            word_list[a] = 'b'
        elif word_list[a] == 'q':
            word_list[a] = 'p'
        elif word_list[a] == 'p':
            word_list[a] = 'q'
    word = ''
    for a in word_list:
        word += a
    print(f'#{_} {word}')