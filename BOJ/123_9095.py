#9095


dp = [ 0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
def solution(num):
	if num == 0:
		return 0
	if dp[num] != 0:
		return (dp[num])
	sum = solution(num-1) + solution(num-2) + solution(num-3)
	dp[num] = sum
	return (sum)
t = int(input())
for _ in range(t):
	n = int(input())
	print(solution(n))

