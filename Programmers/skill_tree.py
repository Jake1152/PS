def solution(skill, skill_trees):
    cnt = 0
    skill_order = list(skill)
    skill_len = len(skill)
    for skill_tree in skill_trees:
        visisted = [False for _ in range(skill_len)]        
        skill_flag = True
        for skill in list(skill_tree):

            if skill in skill_order:
                skill_order_idx = skill_order.index(skill)                
                for idx in range(skill_order_idx):
                    if visisted[idx] == False:
                        skill_flag = False
                        break
                else:
                    visisted[skill_order_idx] = True
            if skill_flag == False:                
                break
        else:
            cnt += 1
    return cnt


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))

'''
이전 스킬이 나오기 전에
이후 스킬이 나오면 fail
단계별로 진행되어야한다.
1. 스킬셋에 들어가는지 여부
2. 스킬 셋에서 순서가 맞는지 여부

"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
'''