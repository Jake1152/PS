n, x = map(int, input().split())
smaller_nums = []
for num in map(int, input().split()):
    if x > num:
        smaller_nums.append(num)
for num in smaller_nums:
    print(num, end=' ')