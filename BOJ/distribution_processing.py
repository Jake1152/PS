import sys
input = sys.stdin.readline
print = sys.stdout.write
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    one_digit_len = 1
    prev_one_digit = a
    prev_num = a
    for pow in range(2, b+1):
        cur_num = prev_num * a
        one_digit = cur_num % 10
        if prev_one_digit == one_digit:
            break
        prev_one_digit = one_digit
        one_digit_len += 1
    # print(f"{one_digit_len=}\n")
    power = b % one_digit_len
    if (power <= 1):
        power = one_digit_len
    # print(f"{power=}\n")
    print(str((a ** power) % 10)+'\n')
