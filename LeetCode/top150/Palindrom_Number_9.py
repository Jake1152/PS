import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        x_len = len(x_list)
        half_len = len(x_list)//2
        # 4, 0 1 2 3
        # 5, 0 1 2 3 4
        
        for idx in range(half_len):
            top = x_list[(x_len - 1)- idx]
            bottom = x_list[idx]
            if top != bottom:
                return False
        return True
        
        
