class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence_idx = 0
        for char in t:
            if (subsequence_idx < len(s) and char == s[subsequence_idx]):
                subsequence_idx += 1
        if (subsequence_idx == len(s)):
            return True
        return False
        
