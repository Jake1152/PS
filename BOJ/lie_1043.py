n, m = map(int, input().split())
truth_set = set(list(map(int, input().split()))[1:])
part_groups = []
for _ in range(m):
    current_group = set(list(map(int, input().split()))[1:])
    part_groups.append(current_group)
    if (current_group & truth_set):
        truth_set = truth_set.union(current_group)
result = 0
for current_group in part_groups:
    print(f"{truth_set=}")
    if (truth_set & current_group) == set():
        result += 1
print(result)

'''
거짓말을 듣고 진실을 듣게 되면 거짓말쟁이가 된다.
즉 다음 파티에 진실을 아는 사람이 없으면 거짓말 가능

10 9
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
-----
1 10
2 3 10
-----
1 4

'''