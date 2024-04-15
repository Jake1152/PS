'''
a ~ b 제일 작은 정수를 찾는 것
'''

N, M = map(int, input().split())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

print(f"{num_list=}")
for _ in range(M):
    a, b = map(int, input().split())
    print(f"{a=}, {b=}")

