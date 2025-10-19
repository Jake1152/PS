class Solution:
    def reverseBits(self, n: int) -> int:
        # 4 => 100
        # 001
        # 9 => 1001
        # 1001
        revserse_bit_str = ''
        while n:
          revserse_bit_str += str(n % 2)
          n //= 2
        print(f"revserse_bit_str : {revserse_bit_str}")
        result = 0
        revserse_bit_digits = len(revserse_bit_str) - 1
        for idx, val in enumerate(revserse_bit_str):
          digits = (31 - idx)
          print(f"digits: {digits}")
          result += 2 ** digits
        return result
# 00111001011110000010100101000000

# 8589934464
# 964176192
