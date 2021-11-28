from collections import deque
command_cnt = int(input())
queue = deque()
for _ in range(command_cnt):
    cmd = input().split()
    if len(cmd) >= 2:
        queue.appendleft(cmd[1])

    elif cmd[0] == "front":
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    elif cmd[0] == "back":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)        
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if (len(queue) == 0):
            print(1)
        else:
            print(0)
    elif cmd[0] == "pop":
        if (len(queue) == 0):
            print(-1)
        else:
            print(queue.pop())
        