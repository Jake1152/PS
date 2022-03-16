n, m = map(int, input().split())
pocketmon_dict = dict()
for idx in range(1,n+1):
    pocketmon = input()
    pocketmon_dict[pocketmon] = idx
    pocketmon_dict[str(idx)] = pocketmon
for _ in range(m):
    keyword = input()
    print(pocketmon_dict[keyword])