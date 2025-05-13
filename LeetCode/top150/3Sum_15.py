import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        # 부분집합의 합이 0이 되는 부분집함의 목록을 리스트에 담아서 return한다.
        - n개 중에 3개만 뽑는조합을 구해서 합이 0이 되는 것들만 넣는다.
        - 정렬을 한 뒤, 가능한 것들만 구한다?
          - 어떻게 구할지 고려 필요.
        '''
        output = set()
        TRIPLETS = 3
        for combi in itertools.combinations(nums, TRIPLETS):
            if sum(combi) == 0:
                combi_str = '_'.join([ str(element) for element in sorted(combi) ])
                output.add(combi_str)
               
        # to be list
        result = []
        for combi_str in output:
            result.append([int(ele) for ele in combi_str.split('_')])
        return result
