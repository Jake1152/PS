class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy_nums = [ num for num in nums ]
        print(copy_nums)
        for idx in range(len(nums)):
            k_rotate_idx = (idx - k) % len(nums)
            nums[idx] = copy_nums[k_rotate_idx]
            
