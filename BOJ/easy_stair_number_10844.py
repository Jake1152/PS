# easy stair number 10844

stair_size = int(input())
dp = [[0 for _ in range(10)] for _ in range(stair_size+1)]

# init stair dp 
for i in range(1, 10):
    dp[1][i] = 1
mod = 1000000000
for i in range(2, stair_size+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# print(dp[stair_size])
print(sum(dp[stair_size]) % mod)

# N = int(input())
# dp = [[0]*10 for _ in range(N+1)] 
# MOD = 1000000000

# for i in range(1, 10):
# 	dp[1][i] = 1
# 	for i in range(2, N+1):
# 		for j in range(10): 
# 			if j == 0:
# 				dp[i][j] = dp[i-1][1]
# 			elif j == 9:
# 				dp[i][j] = dp[i-1][8]
# 			else: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# print(sum(dp[N]) % MOD)



# stair_size = int(input())
# dp = [[0 for _ in range(10)] for _ in range(stair_size+1)]

# # init stair dp 
# for i in range(1, 10):
#     dp[1][i] = 1
# mod = 1000000000
# for digit in range(2, stair_size+1):
#     dp[digit][0] = dp[digit-1][1]
#     for i in range(2, 9+1):
#         dp[digit][i] = dp[digit-1][i-1] + dp[digit-1][i+1]
#     dp[digit][9] = dp[digit-1][8] 
# print(dp[stair_size])
# print(sum(dp[stair_size]) % mod)

