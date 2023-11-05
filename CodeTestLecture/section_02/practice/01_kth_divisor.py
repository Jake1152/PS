N, K = map(int, input().split())
divisor_arr = []
for divisor in range(1, N+1):
    if (N % divisor == 0):
        divisor_arr.append(divisor)
if (len(divisor_arr) + 1> K ):
    print(divisor_arr[K-1])
else:
    print(-1)
