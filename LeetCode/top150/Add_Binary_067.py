from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Brute force version
        '''
        1.  문자열을 a,b를 1의 자리부터 더해서 result를 만든다.
          - carray 변수 사용 
        2. result 문자열을 이진수로 계산한다.
        '''
        result_bin = deque()

        min_len_of_two_str  = min(len(a), len(b))
        man_len_of_two_str  = max(len(a), len(b))
        carry = 0
        # 1의 자리부터 시작 
        for idx in range(-1, man_len_of_two_str-man_len_of_two_str, -1):
            sub_sum = int(a[idx]) + int(b[idx]) + carry
            print(f"sub_sum: {sub_sum}")
            if sub_sum == 3:
                carry = 1
                result_bin.appendleft("1")
            elif sub_sum == 2:
                carry = 1
                result_bin.appendleft("0")
            elif sub_sum == 1:
                carry = 0
                result_bin.appendleft("1")
            elif sub_sum == 0:
                carry = 0
                result_bin.appendleft("0")
            else:
                print("Something wrong!!!")
                break
            print(f"result_bin : {result_bin}")
        
        for idx in range(min_len_of_two_str, len(a)):
            sub_sum = int(a[idx]) + carry
            if sub_sum == 2:
                carry = 1
                result_bin.appendleft("0")
            elif sub_sum == 1:
                carry = 0
                result_bin.appendleft("1")
            elif sub_sum == 0:
                carry = 0
                result_bin.appendleft("0")

        for idx in range(min_len_of_two_str, len(b)):
            sub_sum = int(b[idx]) + carry
            if sub_sum == 2:
                carry = 1
                result_bin.appendleft("0")
            elif sub_sum == 1:
                carry = 0
                result_bin.appendleft("1")
            elif sub_sum == 0:
                carry = 0
                result_bin.appendleft("0")
        if carry == 1:
            result_bin.appendleft("1")
        return str("".join(result_bin))
