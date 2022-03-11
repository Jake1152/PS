# 7568 bulk

n = int(input())
bulks = []
for org_idx in range(n):
    weight, height = map(int, input().split())
    bulks.append([weight, height, org_idx])

for c in bulks:
    rank = 1
    for n in bulks:
        if (c[0] != n)


'''
n = int(input())
bulks = []
for org_idx in range(n):
    weight, height = map(int, input().split())
    bulks.append([weight, height, org_idx])

bulks.sort(key=lambda x: (x[1], x[0]), reverse=True)
print(f"after 1 sort {bulks=}")
prev_weight, prev_height, prev_idx = bulks[0]
number = 1
complement = 0

for i, i_val in enumerate(bulks):
    i_weight, i_height = i_val[0], i_val[1]
    next_i = i+1
    #마지막 항
    if next_i == len(bulks):
        number += complement
        bulks[i].append(number)
        break
    j_weight, j_height = bulks[next_i][0], bulks[next_i][1]
    if (i_weight > j_weight and i_height > j_height):
        number += complement
        bulks[i].append(number)
        number += 1
    else:
        bulks[i].append(number)
        complement += 1

print(f"after {bulks=}")
bulks[len(bulks)-1].append(number)
bulks.sort(key=lambda x: (x[2]))
print(f"finally {bulks=}")
for _, _, _, number in bulks:
    print(number, end=' ')
'''
