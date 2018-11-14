T = int(input())


def super_set_detect():
    len_a = int(input())
    set_a = set(list(map(int, input().split(' '))))

    len_b = int(input())
    set_b = set(list(map(int, input().split(' '))))

    print(set_a.issubset(set_b))


for _ in range(T):
    super_set_detect()