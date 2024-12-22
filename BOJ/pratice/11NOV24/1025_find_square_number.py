N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input())))
print(f"{board=}")

'''
1. 등차수열 경우들을 구한다.
   자릿수별로 진행
   최대 자릿수 max(N, M)
2. 등차수열로 선택된 숫자들을 하나의 숫자로 이어붙인다.
3. 2.에서 이어붙인 숫자가 완전 제곱수인지 판별한다.
'''

''' 등차수열 구하기
1, 1, 1
- n씩 증가 감소
  행이 1씩 증가, 1씩 감소
  열이 1씩 증가, 1씩 감소
- 시작위치를 바꿀 수 있다.
  어떻게 바꿀 수 있는가?
  일일이?
  더 효율적인 방법은 무엇이 있는가?
'''
def get_sequnece_cases(digit):
    sequence_cases = []
    start_pos = [0, 0]

    # for in range():
    return sequence_cases

def concat_number(case):
    return int(''.join(case))

def check_complete_square_number(number):
    square_root_number = int(number ** 0.5)

    if (number == square_root_number ** 2):
        return True
    return False

if '__name__' == '__main__':
    max_square_number = -1
    max_digit = max(N, M)
    for digit in range(max_digit, 0, -1):
        sequence_cases = get_sequnece_cases(digit)
        for sequence in sequence_cases:
            number = concat_number(sequence)
            if check_complete_square_number(number) and \
                number > max_square_number:
                max_square_number = number