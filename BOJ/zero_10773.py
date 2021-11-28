from sys import stdin
input = stdin.readline

cnt = int(input())
num_stack = []
for _ in range(cnt):
    n = int(input())
    if n != 0:
        num_stack.append(n)
    else:
        num_stack.pop()
print(sum(num_stack))