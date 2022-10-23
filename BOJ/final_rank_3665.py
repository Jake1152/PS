# final_rank_3665.py
from collections import deque

test_cnt = int(input())
for _ in range(test_cnt):
    team_cnt = int(input())
    prev_rank = [0]
    prev_rank += list(map(int, input())) # 1부터 시작하게 만듦
    changed_pair_cnt = int(input())
    rank_entry_degree = [ 0 for _ in range(1 + team_cnt)] # 1부터 시작하게 만듦
    rank_candidate = { rank : deque() for rank in range(1, 1 + team_cnt)}
    for _ in range (changed_pair_cnt):
        lhs_rank, rhs_rank = map(int, input().split())
        for rank in range(1, prev_rank[rhs_rank]):
            rank_entry_degree[rank_entry_degree] += 1
            rank_candidate[rank].append(rank)
    final_rank = [rank for rank in prev_rank]
    for rank, entry_degree in enumerate(rank_entry_degree[1:]):
        if entry_degree == 0:
            

