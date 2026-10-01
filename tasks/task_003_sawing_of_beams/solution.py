
def cost_calculation(l: int, sections: list) -> int:
    """
    Принимает l: длину бруса, sections: места, в которых нужно сделать распилы,
    возврощает минимальную стоимость распила.

    """
    points = [0] + sections + [l]
    n_points = len(points)
    dp = [[0] * n_points for _ in range(n_points)]

    for length in range(2, n_points):
        for i in range(n_points - length):
            j = i + length

            current_cost = points[j] - points[i]

            best = float('inf')
            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j]
                if cost < best:
                    best = cost

            dp[i][j] = current_cost + best

    return dp[0][n_points - 1]


def main():

    line1 = input().split()
    l = int(line1[0]) # длина бруса
    n = int(line1[1]) # количество распилов

    sections = list(map(int, input().split())) # места, в которых нужно сделать распилы

    print(cost_calculation(l, sections))


if __name__ == '__main__':
    main()
