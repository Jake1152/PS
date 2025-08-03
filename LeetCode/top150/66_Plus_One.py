class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        digits_size = len(digits) - 1
        for idx, digit in enumerate(digits):
            num += (10 ** (digits_size - idx)) * digit
        num_list = [int(num_val) for num_val in list(str(num + 1))]
        return num_list
