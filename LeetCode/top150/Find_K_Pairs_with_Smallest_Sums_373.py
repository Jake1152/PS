class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        - 중복 순열이 가능함
        - 양쪽 배열 둘다에서 쓰였던 조합이 또 쓰일 수는 없음
        - 한쪽은 이미 쓰였더라도, 다른 한쪽은 안 쓰였었어야 가능함 
        - 둘 다 동시에 같은 조합으로 쓰였다면 쓰일 수 없음
        - 중복순열을 쓰는 것이 편할 것인가?
        각각 10만개 이기에 중복순열 가짓수가 100억개
        다 나열하면 구할 수 없음
        - 오름차순임을 이용해야함
          - 
        '''
        nums1_idx, nums2_idx = 0
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        #  nums1의 idx는 nums1_len을 넘어서는 안됨
        #  nums2의 idx는 nums2_len을 넘어서는 안됨
        visit_set = set()
        # (0, 0), (0, 1)
        while True:
            if nums1_idx >= nums1_len:
                nums1_idx -= 1

            if nums2_idx >= nums2_len:
                nums2_idx -= 1
        
        last_smallest_sum = 0
        for in nums1:
            for in nums2:
              if last_smallest_sum
               




        
