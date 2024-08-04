from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_element_dict = defaultdict(int)
        for num in nums:
            majority_element_dict[num] += 1

        max_key = max(majority_element_dict, key=majority_element_dict.get)
        
        return max_key
