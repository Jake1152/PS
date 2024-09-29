
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (len(preorder) < 1):
            return None
        root = TreeNode(preorder[0])
        prev_node = root

        return root
        # return [3,9,20,None ,None ,15,7]

'''
pre,in-order 리스트를 이용해서
binary tree를 만든다.
이전 노드의 왼쪽, 오른쪽이 누군지 알게한다.

어떻게 할 것인가?
특징이 무엇인가?
맨 앞에 있는 것은 확실하게 root이다.

PRE P, L, R, ...
IN L, P, R
POST L, R, P

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
'''
