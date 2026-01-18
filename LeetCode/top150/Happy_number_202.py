class Solution:
    def isHappy(self, n: int) -> bool:
        LOOP_LIMIT = 10000
        count = 0 
        while (n):
            count += 1
            num_digits = list(str(n))
            result = 0
            for str_num in num_digits:
                num = int(str_num)
                result += num ** 2
            n = result
            if count > LOOP_LIMIT:
                return False
            if n == 1:
                break
        return True
