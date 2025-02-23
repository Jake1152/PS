class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for start_idx in range(len(haystack)):
            if haystack[start_idx:start_idx+needle_len] == needle:
                return start_idx
        return -1
