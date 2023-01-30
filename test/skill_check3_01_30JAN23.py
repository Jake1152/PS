def solution(n, selected_row, cmd):
    answer = ''
    deleted_row_stack = []
    original = [num for num in range(n)]
    work_table = [num for num in range(n)]
    for cur_cmd in cmd:
        print(f"{cur_cmd=}")
        cmd_type = cur_cmd[0]  
        if (cmd_type != "C" and cmd_type != "Z"):
            cmd_val = int(cur_cmd[2])
        cmd_val = int(cmd_val)
        if cmd_type == "D":
            selected_row += cmd_val
            if selected_row > len(work_table):
                selected_row = len(work_table)
        elif cmd_type == "U":
            selected_row -= cmd_val
            if selected_row < 0:
                selected_row = 0
        elif cmd_type == "C":
            deleted_row_stack.append((selected_row, work_table[selected_row]))
            work_table = work_table[:selected_row] + work_table[selected_row + 1:]
            if selected_row > len(work_table):
                selected_row = len(work_table)
        elif cmd_type == "Z":
            prev_position, value = deleted_row_stack.pop()
            work_table = work_table[:prev_position] + [value] + work_table[prev_position:]
            selected_row += 1
    print(f"{work_table=}")
    # print(f"{original=}")
    for num in range(n):
        work_table 
        if org == cur:
            answer.append("0")
        else:
            answer.append("X")

    for cur in work_table:
        
        if org == cur:
            answer.append("0")
        else:
            answer.append("X")
    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"] 
print(solution(n, k, cmd))