import sys
sys.setrecursionlimit(10**4)
A_MAX = 1001
B_MAX = 1001

lcs_table = [ [-1 for _ in range(A_MAX)] for _ in range(B_MAX)]

first_str = input()
second_str = input()

def lcs_len(a_str, b_str, a_idx, b_idx):
	# 종료 조건 두 문자열 중 하나가 빈 문자열일때
	# LCS_LEN은 0이 된다.
	if (a_idx == 0 or b_idx == 0):
		return 0
	
	# 이미 캐시에 계산된 값이 있다면 (-1이 아니라면)
	# 캐시의 값을 반홚나다.
	if (lcs_table[a_idx][b_idx] != -1):
		return lcs_table[a_idx][b_idx]
	
	# 문자열의 마지막 글자를 비교 조건에 따라 재귀 호출
	if (a_str[a_idx - 1] == b_str[b_idx - 1]):
		lcs_table[a_idx][b_idx] = 1 + lcs_table(a_str, b_str, a_idx - 1, b_idx - 1)
	else:
		lcs_table[a_idx][b_idx] = max(lcs_len(a_str, b_str, a_idx, b_idx - 1), \
									lcs_len(a_str, b_str, a_idx - 1, b_idx))
	return (lcs_table[a_idx][b_idx])

print(lcs_len(first_str, second_str, len(first_str), len(second_str)))