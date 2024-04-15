import sys
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# dp = []
'''
'''
def bfs(cur_coordinates):
    count = 0
    queue = [cur_coordinates]
    while (queue):
        row, col = queue.pop()
        step_size = board[row][col]
        if (row == N-1 and col == N-1):
            count += 1
            continue
        if (row + step_size) < N:
            queue.append((row + step_size, col))
        if (col + step_size) < N:
            queue.append((row, col + step_size))
    return count
print(bfs((0, 0)))
