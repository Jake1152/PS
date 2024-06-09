class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        # other1
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        # other2
        for j in range(n):
          nums1[m+j] = nums2[j]
        nums1.sort()


        # result = []

        # idx_i = 0
        # idx_j = 0
        # copy_nums1 = [element for element in nums1]
        
        # idx = 0
        # min_nums1 = 0
        # if (nums1):
        #     min_nums1 = nums1[0]
        # min_nums2 = 0
        # if (nums2):
        #     min_nums2 = nums2[0]
        # prev_value = min(min_nums1, min_nums2)
        # while (idx < m + n and idx_i < m and idx_j < n):
        #     if (prev_value > copy_nums1[idx_i]):
        #         idx_i += 1
        #         continue
            
        #     if (prev_value > nums2[idx_j]):
        #         idx_j += 1
        #         continue
            
        #     if (copy_nums1[idx_i] < nums2[idx_j]):
        #         nums1[idx] = copy_nums1[idx_i]
        #         prev_value = nums1[idx]
        #         idx_i += 1
        #         idx += 1
        #     elif (copy_nums1[idx_i] >= nums2[idx_j]):
        #         nums1[idx] = nums2[idx_j]
        #         prev_value = nums1[idx]
        #         idx_j += 1
        #         idx += 1
        # while (idx < n + m and idx_i < m):
        #     nums1[idx] = copy_nums1[idx_i]
        #     prev_value = nums1[idx]
        #     idx_i += 1
        #     idx += 1
        
        # while (idx < n + m and idx_j < n):
        #     nums1[idx] = nums2[idx_j]
        #     prev_value = nums1[idx]
        #     idx_j += 1
        #     idx += 1
        
   
        """
        Do not return anything, modify nums1 in-place instead.
        """
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol = Solution()
sol.merge(nums1, m, nums2, n)
print(f"{nums1 =}")