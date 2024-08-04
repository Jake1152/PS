from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_alphabet_dict = defaultdict(int)
        for ch in magazine:
            magazine_alphabet_dict[ch] += 1
        
        for ch in ransomNote:
            magazine_alphabet_dict[ch] -= 1
        
        for key, value in magazine_alphabet_dict.items():
            if value < 0:
                return False
        return True

        
