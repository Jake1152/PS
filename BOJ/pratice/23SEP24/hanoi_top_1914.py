# hanoi_top_1914.py
# import sys

# input = sys.stdin.readline()
disk_count = int(input())
# for _ in range(disk_count):
#     pass

'''
n-1개 원반을 temp로 옮긴다.
가장 칸 원반은 destination으로 옮긴다.
그 다음 작은 원반들(n - 2)은 현재 비어있는 source에 옮기고
다음으로 가장 큰 원반(n - 1)을 destination으로 옮긴다.
disk가 0이 될때까지 옮긴다.
-------
n - 1개는 temp로 옮긴다.
n 번쨰를 목표지점으로 옮긴다.
n 

현재꺼는 출력할 것이니까 재귀 돌릴 필요가 없다.
'''
# move_count += 1
# if (disk <= 0):
#     print(move_count)
#     return 
move_count = 0
print_list = []

def hanoi_top(source, temp, destination, disk):
    global move_count, print_list

    if disk <= 0:
        return 
    move_count += 1
    # print()
    hanoi_top(source, destination, temp, disk - 1)
    if disk_count <= 20:
        print_list.append(" ".join([source, destination]))
    hanoi_top(temp, source, destination, disk - 1)


hanoi_top("1","2","3", disk_count)
print(move_count)
for move_history in print_list:
    print(move_history)