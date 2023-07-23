from collections import deque

def is_can_be_solved(ability, problem):
    cur_alp = ability[0]
    cur_cop = ability[1]
    problem_alp = problem[0]
    problem_cop = problem[1]
    if (cur_alp < problem_alp) or (cur_cop < problem_cop):
        return (False)
    return (True)

'''
최단경로로 가장 빠르게 연습할 수 있는 방법을 찾는다.

소요된 시간을 return한다.
'''
def practice(problem, solved_list):
    if (solved_list):
        pass
    pass

def solution(alp, cop, problems):
    answer = 0
    solved_list = []
    asc_problems = deque(sorted(problems, key=lambda x: (x[0] + x[1], x[0],  x[1])))
    for problem in asc_problems:
        # print(f"{problem=}")
        if is_can_be_solved((alp, cop), problem) == False:
            answer += practice(problem)
            
    return answer