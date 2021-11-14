from sys import stdin, stdout
input = stdin.readline
print = stdout.write
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(str(a + b)+'\n')
