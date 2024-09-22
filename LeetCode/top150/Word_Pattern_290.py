class Solution:
    def checkDuplicateWordInDict(pattern_dict: dict, pattern_alphabet: str, word: str) -> bool:
        for key, value in pattern_dict.items():
            if key != pattern_alphabet and word == value:
                return True
        return False

    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        pattern_dict = dict()
        for pattern_alphabet, word in zip(pattern, s_list):
            if (pattern_dict.get(pattern_alphabet) and pattern_dict[pattern_alphabet] != word):
                return False
            else:
                if Solution.checkDuplicateWordInDict(pattern_dict, pattern_alphabet, word):
                    return False
                pattern_dict[pattern_alphabet] = word
        return True
