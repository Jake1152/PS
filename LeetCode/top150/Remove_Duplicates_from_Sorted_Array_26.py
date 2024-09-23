class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy_nums = [ num for num in nums ]
        prev = ''
        cur_idx = 0
        for num in copy_nums:
            if (prev != num):
                nums[cur_idx] = num
                prev = num
                cur_idx += 1
        return cur_idx
        
