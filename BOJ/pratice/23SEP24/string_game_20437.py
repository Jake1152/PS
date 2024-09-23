'''
1. 알파벳 소문자로 이루어진 문자열 w가 주어짐
2. 양의 정수 k가 주어짐
3. 어떤 문자를 정확히 k개를 포함하는 가장 짧은 연속 문자열의 길이를 구함
4. 어떤 문자를 정확히 k개를 포함하고, 문자열의 첫 번째와 
   마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

# 출력
T개의 줄 ehddks answkduf rpdladml 3,4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.
만족하는 연속 문자열이 없을 시 -1 출력



'''

from collections import defaultdict

T = int(input())
for _ in range(T):
   W = input()
   K = int(input())
   alpha_dict = defaultdict(int)
   for ch in W:
      print(f"{ch=}")
      alpha_dict[ch] += 1
   print(f"{alpha_dict=}")
