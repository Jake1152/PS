#AC 5430

from collections import deque
import re

def cmd_list_diet(cmd_list):
    return_list = []
    prev_cmd = ''
    rotate_cnt = 0    
    for cmd in cmd_list:
        if cmd == 'R':
            rotate_cnt += 1
            continue
        elif cmd != 'R' and prev_cmd == 'R' and rotate_cnt % 2 != 0:
            return_list.append(cmd)
            prev_cmd = cmd
            rotate_cnt = 0
        else:
            return_list.append(cmd)
    return return_list

test_case = int(input())
for _ in range(test_case):
    
    cmd_list = list(input())
    print(f"{cmd_list=}")
    cutted_cmd_list = cmd_list_diet(cmd_list)
    print(f"{cutted_cmd_list=}")
    list_len = int(input())
    given_list = input().split(',')
    given_list[0] = given_list[0][-1]
    given_list[-1] = given_list[-1][0]
    #list(map(int,))
    print(f"{given_list=}")
    # for cmd in cmd_list:
        


