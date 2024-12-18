'''
산봉우리마다 경비원을 배치
이를 위해 농장에 산봉우리가 총 몇 개 있는지 세는 것이 문제 

산봉우리의 정의는 다음과 같다.
산봉우리는 같은 높이를 가지는 하나의 격자 
혹은 인접한 격자들의 집합으로 이루어져 있다.

여기서 인접하다의 정의는 X좌표 차이와 Y좌표 차이가 모두 1 이하인 경우이다. => 가운데 기준 8방향 좌표
또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.
'''
N, M = map(int, input().split())
farm = []
for _ in range(N):
    farm.append(list(map(int, input().split())))
print(f"{farm=}")
