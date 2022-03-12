#heap 1927 
from sys import stdin
import heapq

input = stdin.readline
heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)