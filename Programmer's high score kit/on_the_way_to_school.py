# on the way to school
def solution(m, n, puddles):
    area = [[ 0 for _ in range(m + 1)] for _ in range(n + 1)]
    for coordinates in puddles:
        x = coordinates[0]
        y = coordinates[1]
        area[y][x] = -1
    area[1][1] = 1
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if area[row][col] != -1:
                if area[row - 1][col] != -1:
                    area[row][col] += area[row - 1][col]
                if area[row][col - 1] != -1:
                    area[row][col] += area[row][col - 1]
    return area[n][m] % 1000000007