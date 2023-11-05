N, K = map(int, input().split())
# divisor_arr = []
cnt = 0
for divisor in range(1, N+1):
    if (N % divisor == 0):
        K -= 1
    if K == 0:
        print(divisor)
        break
else:
    print(-1)
    
# if (len(divisor_arr) + 1> K ):
#     print(divisor_arr[K-1])
# else:
#     print(-1)
