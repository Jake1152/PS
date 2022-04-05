test_case = int(input())
for _ in range(test_case):
	buildings, construction_rules = map(int, input().split())
	construction_durations = list(map(int, input().split()))
	from_build, to_build = map(int, input().split())
