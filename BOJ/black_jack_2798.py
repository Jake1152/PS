# black_jack_2798
from itertools import permutations

n, m = map(int, input().split())
card_list = sorted(list(map(int, input().split())))
for idx, val in enumerate(card_list):
    if val > m:
        card_list = card_list[:idx][::-1]
# 내림차순으로 된 card list
near_num = 300000
for permute_num in permutations(card_list, 3):
    gap = m - sum(permute_num)
    if gap >= 0 and near_num > gap:
        near_num = gap
    if near_num == 0:
        break
print(m - near_num)