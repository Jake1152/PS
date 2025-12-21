class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums = list(set(nums))
        len_nums = len(nums)
        for i_idx in range(len_nums//2):
            j_idx = len_nums - i_idx  - 1 if len_nums - i_idx > 0 else len_nums - i_idx
            print(f"{len_nums=},\t{i_idx=},\t{j_idx=}")
            if nums[i_idx] == nums[j_idx] and abs(i_idx - j_idx) <= k:
                return True
        return False
