# 1497 guitar_concert
from itertools import combinations

# 조합을 1개씩 시작하면서 최대 갯수와 같으면 break하고 출력
def solution(max_playing_cnt, guitars, guitar_cnt):
	min_guitars_for_playing = -1
	if max_playing_cnt == 0:
		return(min_guitars_for_playing)
	else:
		comb_cnt = 1
		while (comb_cnt <= guitar_cnt):
			for comb in combinations(guitars, comb_cnt):
				merge_set = set()
				for each_set in comb:
					merge_set = merge_set.union(each_set)
				if max_playing_cnt == len(merge_set):
					return (comb_cnt)
			comb_cnt += 1
		return (comb_cnt)

guitar_cnt, play_cnt = map(int, input().split())
guitars = []

# 기타list에 play 가능한 곡들을 set으로 담아준다.
for _ in range(guitar_cnt):
	guitar, playlist = input().split()
	tmp_set = set()
	for idx, song in enumerate(list(playlist)):
		if song == 'Y':
			tmp_set.add(idx)            
	guitars.append(tmp_set)

# 모든 기타에 플레이 가능한 경우를 집합으로 합침
all_play_set = set()
for playset in guitars:
	# print(f"{playset=}")
	all_play_set = all_play_set.union(playset)
	# print(f"{all_play_set=} in loop")
# 전체 플레이 가능한 곡 개수
max_playing_cnt = len(all_play_set)


print(solution(max_playing_cnt, guitars, guitar_cnt))
'''
# a_set = set({1,2,34,5})
# b_set = set({1,2,6})

# # print(a_set)
# print(a_set.union(b_set))
'''
