def solution(board, skills):
    answer = 0
    # 스킬 수만큼 반복
    # 25만 * 100만 => 2500억
    dp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    '''
    0~n까지만 하는게 아니라 n+1지점에 상쇄할 수 있는 값을 넣는 이유
    전체영역에 누적합부분을 한번에 더하는 연산으로 처리할 수 있게하기 위함 
    0~2까지 영역에 N을 더하는 것 이라면 아래와 같이 4개의 꼭지점을 표현한다 
    
    0. 누적 초기
    [ [N, 0, 0, -N, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [-N, 0, 0, N, 0] ]
    => 1. 행 우선 누적
    [ [N, N, N, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [-N, -N, -N, 0, 0] ]
    => 2. 열 우선 누적
    [ [N, N, N, 0, 0],
      [N, N, N, 0, 0],
      [N, N, N, 0, 0],
      [0, 0, 0, 0, 0] ]
    => 3. 전체 영역 누적 

    '''
    for skill in skills:
        skill_type, r1, c1, r2, c2, degree = skill
        dp[r1][c1] += degree if skill_type == 2 else -degree
        dp[r1][c2+1] += -degree if skill_type == 2 else degree
        dp[r2 + 1][c1] += -degree if skill_type == 2 else degree
        dp[r2 + 1][c2 + 1] += degree if skill_type == 2 else -degree
        print(f"#{dp=}")

    # 맵에 있는 건물들 순회하며 degree 더하기
    #  행 기준 누적합
    for x in range(len(dp) - 1):
        for y in range(len(dp[0])-1):
            dp[x][y + 1] += dp[x][y]
    #  열 기준 누적합
    for y in range(len(dp[0]) - 1):
        for x in range(len(dp) - 1):
            dp[x + 1][y] += dp[x][y]
    # 기존 배열과 누적 배열의 합 and 살아남은 건물 카운팅
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] += dp[x][y]
            if board[x][y] > 0:
                answer += 1
    return answer



# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill= [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# print(f"{solution(board, skill)=}")