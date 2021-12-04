t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)

'''
org version

T = int(input())
# memo = {1: 1, 2: 1}
zero_cnt = 0
one_cnt = 0

for _ in range(T):
    n = int(input())
    
def fib(num):
    if num == 0:
        zero_cnt += 1    
    elif num == 1 or num == 1:
        one_cnt += 1
    else:        
        return fib(num-1) + fib(num-2)

'''