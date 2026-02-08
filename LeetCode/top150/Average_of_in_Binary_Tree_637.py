# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        level order진행
        queue에 값을 담아둔다.
        '''
        queue = deque()
        queue.append(root)
        result = []
        while (queue):
            level_size = len(queue)
            cur_level_sum = 0
            for _ in range(level_size):
                cur = queue.popleft()
                cur_level_sum += cur.val
                if cur:
                    # print(f"{cur.val}")
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
            result.append(cur_level_sum/level_size)
        return result

