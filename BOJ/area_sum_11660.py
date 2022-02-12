N, M = map(int, input().split())
square = [[0] for _ in range(N+1)]
for row in range(N):
    square[row] += list(map(int, input().split()))
# 행별로 이전 셀까지의 값을 누적.
for row in range(1, N+1):
    for col in range(1, N+1):
        square[row][col] = square[row][col-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    area_sum = 0
    for row in range(x1, x2+1):
        area_sum += square[row][y2] - square[row][y1]
