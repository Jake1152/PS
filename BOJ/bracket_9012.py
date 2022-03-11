# 9012
n = int(input())
for _ in range(n):
    stack = []
    flag = True
    bracket_list = list(input())
    for bracket in bracket_list:
        if bracket == "(":
            stack.append(bracket)
        else:
            if (stack == [] or stack.pop() == bracket):
                flag = False
                break
    if (stack == [] and flag):
        print("YES")
    else:
        print("NO")