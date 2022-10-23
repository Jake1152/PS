n, k = map(int, input().split())
result = 1
for num in range (n, n - k, -1):
    result *= num
    
for num in range (k, 0, -1):
    result //= num

print(result % 10007)