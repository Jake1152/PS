to_be_self_num = set([i for i in range(1, 10000+1)])
constructor_list = []
for num in range(1, 10000 + 1):
    sum = 0
    sum += num
    for n in list(str(num)):
        sum += int(n)
    constructor_list.append(sum)
for self_num in sorted(to_be_self_num - set(constructor_list)):
    print(self_num)