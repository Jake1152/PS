# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_one, node_two = l1, l2
        ret = ListNode()
        cur = ret
        supplement_value = 0
        while (node_two or node_one):
            cur_value = 0
            if node_one:
               cur_value += node_one.val
               node_one = node_one.next
            if node_two:
               cur_value += node_two.val
               node_two = node_two.next
            cur_value += supplement_value
            temp = ListNode(cur_value % 10)
            supplement_value = cur_value // 10
            print()
            cur.next  = temp
            cur = temp
        if (supplement_value):
            cur.next = ListNode(supplement_value)
            
        return ret.next
