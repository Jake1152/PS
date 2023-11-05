def solution(board, skills):
    answer = 0
    for skill in skills:
        skill_type, r1, c1, r2, c2, degree = skill
        degree = -degree if skill_type == 1 else degree
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                board[x][y] += degree
    for rows in board:
        for element in rows:
            if element > 0:
                answer += 1
    return answer

