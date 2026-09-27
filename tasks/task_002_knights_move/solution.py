
def board_size(n):
    """
    Принимает список из 2 чисел. Клетки N x M на шахматной доске
    """
    a = int(n[0])
    b = int(n[1])
    dp = [[0] * b for _ in range(a)]
    dp[0][0] = 1
    for i in range(a):
        for j in range(b):

            if i >= 2 and j >= 1:
                dp[i][j] += dp[i - 2][j - 1]
            if i >= 1 and j >= 2:
                dp[i][j] += dp[i - 1][j - 2]

    return dp[a - 1][b - 1]

def main():
    n = list(map(int, input().split()))
    print(board_size(n))


if __name__ == '__main__':
    main()