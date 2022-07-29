import sys

sys.stdin = open("_암호문1.txt")

for _ in range(1, 11):
    T = int(input())
    original_list = input().split()
    N = int(input())
    order_list = input().split()
    for a in range(len(order_list)):
        add_list = []
        result_list = []
        if order_list[a] == 'I':
            index_number = int(order_list[a + 1])
            number_amnt = int(order_list[a + 2])
            for b in range(a + 3, a + 3 + number_amnt):
                add_list.append(order_list[b])
            for c in range(len(original_list)):
                if c != index_number:
                    result_list.append(original_list[c])
                else:
                    for d in range(len(add_list)):
                        result_list.append(add_list[d])
                    result_list.append(original_list[c])
            original_list = result_list
    print(f'#{_} ', end = '')
    for i in range(10):
        if i == 9:
            print(int(original_list[i]))
        else:
            print(int(original_list[i]), end = ' ')