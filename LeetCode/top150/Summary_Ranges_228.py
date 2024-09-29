class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        def concatRangeInfo(sequence_info: dict) -> str:
            cur = ""
            cur += str(sequence_info["start_num"])
            if (sequence_info["start_num"] != sequence_info["last_num"]):
                cur += "->"
                cur += str(sequence_info["last_num"])
            return cur

        result = []
        if len(nums) < 1:
            return result
        prev_num = nums[0]
        sequence_info = { "start_num": nums[0], "last_num": nums[0] }
        for num in nums[1:]:
            if num > prev_num + 1:
                concat_range_str = concatRangeInfo(sequence_info)
                result.append(concat_range_str)
                sequence_info["start_num"] = num
                sequence_info["last_num"] = num
            else:
                sequence_info["last_num"] = num
            prev_num = num
        else:
            concat_range_str = concatRangeInfo(sequence_info)
            result.append(concat_range_str)
        return result
