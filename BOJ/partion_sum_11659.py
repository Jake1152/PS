import sys
input = sys.stdin.readline
print = sys.stdout.write
list_len, test_case = map(int, input().split())
num_list = [0]
num_list += list(map(int, input().split()))
dp = [ 0 for _ in range(list_len+1)]
dp[0] = num_list[0]
for idx in range(1, list_len+1):
    dp[idx] += dp[idx-1] + num_list[idx]
for _ in range(test_case):
    start, end = map(int, input().split())
    print(str(dp[end] - dp[start-1])+'\n')