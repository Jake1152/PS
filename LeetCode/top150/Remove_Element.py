class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0

        for idx, num in enumerate(nums):
            if num == val:
                val_count += 1
            else:
                nums[idx - val_count] = num
        return len(nums) - val_count
