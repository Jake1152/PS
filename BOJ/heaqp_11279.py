import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(str(heapq.heappop(heap)[1]))
        else:
            print(str(0))
    else:
        heapq.heappush(heap, [-x, x])