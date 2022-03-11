from itertools import combinations

while (True):
	test_case = list(map(int, input().split()))
	if test_case[0] == 0:
		break
	k = test_case[0]
	for case in combinations(test_case[1:], 6):
		print(' '.join(map(str, case)))
	print()