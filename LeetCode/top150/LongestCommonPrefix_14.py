class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        prev_prefix = ""
        if len(strs[0]) > 0:
            prev_prefix = strs[0][0]
        for cur_idx in range(shortest_length):
            prev_prefix = strs[0][cur_idx]
            for word in strs:
                if prev_prefix != word[cur_idx]:
                    return longest_common_prefix
            longest_common_prefix += prev_prefix
        return longest_common_prefix
