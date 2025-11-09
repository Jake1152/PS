class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.split()
        return ' '.join(str_list[::-1])
