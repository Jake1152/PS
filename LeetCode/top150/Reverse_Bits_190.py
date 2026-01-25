class Solution:
    def reverseBits(self, n: int) -> int:
        bin_str = str(bin(n))
        revserse_bit_str = (bin_str[2:])[::-1]

        SINGED_INT_LEN =32
        while (len(revserse_bit_str)<SINGED_INT_LEN):
            revserse_bit_str += '0'
        result = int(revserse_bit_str, 2)
        return result
