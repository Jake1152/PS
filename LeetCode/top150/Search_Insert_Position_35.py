class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums.find
        begin = 0
        end = len(nums) - 1
        mid = 0
        while begin <= end:
            mid = (begin + end) // 2
            if mid > -1 and nums[mid] > target:
              end = end - 1
            elif nums[mid] < target:
              begin = begin + 1
            else:
              break
        result = mid
        if nums[mid] > target:
          result = mid
        elif nums[mid] < target:
          result = mid + 1
        return result
