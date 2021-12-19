n = int(input())
sequence_a = list(map(int, input().split()))
dp = [ 0 for _ in range(n)]
result = 0
dp[0] = sequence_a[0]
# 앞에서부터 한개씩 진행 현재 숫자가 가장 마지막에 위치한다는 가정
for i in range(1, n):
    max = 0
    # 내 앞에 있는 순열들 중 증가수열이 되게하는 수열 중 가장 큰 값 선택
    for j in range(0,i):
        if sequence_a[j] < sequence_a[i] and dp[j] > max:
            max = dp[j]
    dp[i] = max + sequence_a[i]
    if dp[i] > result:
        result = dp[i]
print(result)        
    