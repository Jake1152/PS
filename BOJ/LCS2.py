import sys
sys.setrecursionlimit(10**9)

a = [0] + list(input())
b = [0] + list(input())
len_a = len(a)
len_b = len(b)
dp = [[""] * len_b for i in range(len_a)]
print(f"{dp=}")
for i in range(1, len_a):
	for j in range(1, len_b):
		if a[i] == b[j]:
			dp[i][j] = dp[i - 1][j - 1] + a[i]
			print(f"{i=}, {j=}, {a[i]=}")
			# break
		else:
			if len(dp[i - 1][j]) > len(dp[i][j - 1]):
				dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i][j - 1]
		print(f"{dp=} in loop")
print(f"\n\n\n{dp=}")
lcs_len = len(dp[len_a - 1][len_b - 1])
print(lcs_len)
if lcs_len:
    print(dp[len_a - 1][len_b - 1])
# import sys
# sys.setrecursionlimit(10**9)

# STR_MAX = 1001
# lcs_list = []
# lcs_table = [[0 for _ in range(STR_MAX)] for _ in range(STR_MAX)]
# a_visited = [ True for _ in range(STR_MAX)]
# b_visited = [ True for _ in range(STR_MAX)]

# def lcs_search(a_str, b_str, a_idx, b_idx):
# 	if a_idx == 0 or b_idx == 0:
# 		return 0
	
# 	if lcs_table[a_idx][b_idx] != 0:
# 		return lcs_table[a_idx][b_idx]
	
# 	if a_str[a_idx-1] == b_str[b_idx-1]:
# 		lcs_table[a_idx][b_idx] = 1 + lcs_search(a_str, b_str, a_idx-1, b_idx-1)
# 		for tmp_a_idx in range(a_idx-1):
# 			b_visited[tmp_a_idx] = False
# 		for tmp_b_idx in range(b_idx-1):
# 			b_visited[tmp_b_idx] = False
# 		if (a_visited[a_idx-1] and b_visited[b_idx-1]):
# 			lcs_list.append(a_str[a_idx-1])
			
# 	else:
# 		lcs_table[a_idx][b_idx] = max(lcs_search(a_str, b_str, a_idx-1, b_idx),
# 										lcs_search(a_str, b_str, a_idx, b_idx-1))
# 	return lcs_table[a_idx][b_idx]

# first_str = input()
# second_str = input()
# lcs_len = lcs_search(first_str, second_str, len(first_str), len(second_str))
# print(lcs_len)
# if lcs_len:
# 	print(''.join(lcs_list))