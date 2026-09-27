
def get_median(n):
    """
    Принимает список из 3 чисел, сортирует пузырьком и возвращает медиану.
    """
    if n[0] > n[1]:
        n[0], n[1] = n[1], n[0]
    if n[1] > n[2]:
        n[1], n[2] = n[2], n[1]
    if n[0] > n[1]:
        n[0], n[1] = n[1], n[0]

    return n[1]


def main():
    n = list(map(int, input().split()))
    print(get_median(n))


if __name__ == '__main__':
    main()