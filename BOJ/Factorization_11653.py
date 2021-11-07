# 11653 Factorization
x = int(input())
div = 2
while x != 1:
    if x  % div == 0:
        x /= div
        print(div)
    else:
        div += 1