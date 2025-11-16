# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
같은 방향으로만 순회한다?
한번에 하나씩만 간다?
그렇게 되면 
'''
def post_order(node, result_list):
    if node == None:
      # print("node is null")
      return result_list.append("None")
    #if node.left:
    post_order(node.left, result_list)
    #if node.right:
    post_order(node.right, result_list)
    result_list.append(node.val)

class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #return str(p) == str(q) # Solution 1
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False 
        if p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
