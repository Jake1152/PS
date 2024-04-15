import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())

dp = [ 0 for _ in range(N + 1) ]
if N >= 2:
    dp[1] = 1 # 1
    dp[2] = 2 # 00, 11

def get_makable_binary_sequence_count(number):
    if (number < 1):
        return 0
    if (dp[number]):
        return dp[number]
    #dp[num] = (get_makable_binary_sequence_count(num - 1) + get_makable_binary_sequence_count(num - 2)) % 15746
    for num in range(3, number + 1):
        dp[num] = (dp[num - 1] + dp[num - 2]) % 15746
    return dp[num]

print(get_makable_binary_sequence_count(N))
# for num in range(N):
#     print(num, "case : ", get_makable_binary_sequence_count(num))