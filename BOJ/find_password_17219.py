# find password 17219
from collections import defaultdict
from sys import stdin
input = stdin.readline

site_dict = defaultdict(str)
n, m = map(int, input().split())
for _ in range(n):
    site_addr, password = input().strip().split(' ')
    site_dict[site_addr] = password
for _ in range(m):
    site_addr = input().strip()
    print(site_dict[site_addr])