'''
# 문제이해
- 문제 고르기
- N개 가지고 있고, 모든 문제의 난이도를 정수로 수치화
  i번째 문제의 난이도는 A_i이다. 
- 캠프에 사용할 문제는 두 문제 이상이어야 한다.

  문제가 너무 어려우면 학생들이 멘붕에 빠지고, 
  문제가 너무 쉬우면 학생들이 실망에 빠지게 된다. 
  따라서 문제 난이도의 합은 L보다 크거나 같고, R보다 작거나 같아야 한다.
  또, 다양한 문제를 경험해보기 위해 가장 어려운 문제와 
  가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다.
  캠프에 사용할 문제를 고르는 방법의 수를 구해보자.

# 문제해결방법
- 캠프에 사용할 문제의 수는 두 문제 이상
- L <= sum(levels) <= R
- highest_level - lowest_level <= max_level_difference

2 ~ N개까지 문제를 조합으로 뽑는 경우의 수
조합으로 뽑으면서 가장 쉬운 문제와 어려운 문제의 난이도 차이를 감안한다.

조합으로 다 뽑고서 계산한다?

2C15 + ... + 15C15
2 3 4 5 6 7 8
15 * 7
105, 400, 1200, 3300, 5100, 
'''

from itertools import combinations

problem_count, lowest_level_limit, highest_level_limit, max_level_difference_limit = list(map(int, input().split()))
levels = list(map(int, input().split()))

def check_problem_set_level(problem_set):
  # 문제 난이도 총합
  sum_levels = sum(problem_set)
  # print(f"{problem_set=}")
  # print(f"{sum_levels=}")
  if (lowest_level_limit > sum_levels or 
      highest_level_limit < sum_levels):
    return False

  # 난이도 최대 격차
  max_level_difference = max(problem_set) - min(problem_set)
  # print(f"{max_level_difference=}")
  if (max_level_difference_limit > max_level_difference):
    return False

  return True

if __name__ == '__main__':
  case_count = 0
  for collect_problem_count in range(2, problem_count + 1):
    for problem_set in combinations(levels, collect_problem_count):
      if (check_problem_set_level(problem_set)):
        case_count += 1
  print(case_count)
     


