import sys     
sys.setrecursionlimit(10**9) 


'''
- 포화이진트리를 만듦(루트노드는 그대로 유지)
- 노드들 가장 왼쪽노드부터 가장 오늘쪽 노드까지 왼쪽에 있는 순서대로 살펴봄
  - 노드의 높이는 살펴보는 순서에 영향을 주지 않는다.
- 살펴본 노드가 더미노드라면 문자열 뒤에 0을 추가. 더미가 아니라면 1을 추가
- 이진수를 십진수로 변환 

순회순서는 in-order
'''

'''
# 문제해결방법

1. 주어진 숫자를 이진수로 변환한다.
2. 이진수를 포화이진트리처럼 꽉 채워준다.
3. in-order 순회결과로 표현되는지 확인한다.
  - in-order인지는 비단말노드가 0이어서는 안된다.
  - 비단말 노드를 
## 시간초과가 난다면?
- 서브트리가 될 수 있는 값 중 안되는 것을 찾아야하는가?
- 비단말 노드를 빠르게 찾는다
'''
def solution(numbers):
    answer = []

    # range [) type, start,end는 시작, 끝 index를 의미 0, 15
    def check_nonterminal_node(binary_number, start, end, parent):
        # if length < 0:
        #     return False
        parent_idx = (start + end) // 2
        # print(f"{start=}, {end=}, {(end - start)=}, {parent_idx=}")
        if end - start == 1:
            return  binary_number[parent_idx]
        # print(f"# {binary_number[start:end]=}, {start=}, {end=}, {parent_idx=}, {binary_number[parent_idx]=}")
        if (binary_number[parent_idx] == '1'):
            if parent == '0':
                return False
            return check_nonterminal_node(binary_number, start, parent_idx, binary_number[parent_idx]) and \
                    check_nonterminal_node(binary_number, parent_idx + 1, end, binary_number[parent_idx])
        elif (binary_number[parent_idx] == '0'):
            return check_nonterminal_node(binary_number, start, parent_idx, binary_number[parent_idx]) and \
                    check_nonterminal_node(binary_number, parent_idx + 1, end, binary_number[parent_idx])
        
        
    # 1. 이진수 변환 및 포화이진트리 자릿수로 맞춤 
    '''
    최대 64비트 -> 64자리
    010
    '''
    # length = len(binary_number)
    for number in numbers:
        # 1-1 이진수로 변환
        binary = bin(number)
        binary = binary[2:]
        # print(f"{binary=}")
        # 1-2. 포화이진트리 형태로 변환
        # 2로 계속 나누었을 때 몫이 1이 될때까지 몇번 걸리는가
        cur_binary_number_digit = len(binary)
        # 
        binary_tree_height = 0 
        while (cur_binary_number_digit):
            # print(f"{cur_binary_number_digit=}")
            cur_binary_number_digit = cur_binary_number_digit // 2
            binary_tree_height += 1
        # digit = [binary_tree_height][0]
        complement_digit = (2 ** (binary_tree_height) - 1) - len(binary)
        # print(f"{number=}, {binary_tree_height=}, {binary=}")
        # print(f"{complement_digit=}")
        while (complement_digit):
            binary = "0" + binary
            complement_digit -= 1
        # print(f"# {number=}, {binary_tree_height=}, {binary=}")
        # print(f"# after complementary {binary=}")
        # 2. in-order 일 때 비단말노드가 0인지 확인 
        is_possible_tree = check_nonterminal_node(binary, 0, len(binary), '1')
        # print(f"## {is_possible_tree=}")
        if is_possible_tree:
            answer.append(1)
        else:
            answer.append(0)
        # print()
    return answer


test_case = []
# test_case.append([7,42, 5])
# test_case.append([7,42,5])
# test_case.append([63, 111, 95])
# test_case.append([2147483647, 1073741823, 9223372036854775807])
# test_case.append([64, 63, 42, 33, 32, 31])
test_case.append([64, 63, 42, 255, 511, 1023, 2047, 4095, 8191, 2**15-1, 96, 423])
for number in test_case:
    print(solution(number))
