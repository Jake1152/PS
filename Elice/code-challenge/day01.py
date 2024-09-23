array_size, work_count = map(int, input().split())
arr = [0] + list(map(int, input().split()))
for _ in range(work_count):
    begin, end, kth = map(int, input().split())
    print(sorted(arr[begin:end + 1])[kth - 1])


'''
input
8 3
1 7 6 8 1 6 4 5
1 5 3
2 6 2
4 8 3
'''
