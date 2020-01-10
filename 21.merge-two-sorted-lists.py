#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        current_node = root
        # Equals to 
        # while l1 is not None and l2 is not None:
        while l1 and l2:
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2  
                l2 = l2.next
            
            # This step is required!!!
            current_node = current_node.next
        
        # Equals to
        # if l1 is not None:
        #     current_node.next = l1
        # elif l2 is not None:
        #     current_node.next = l2
        current_node.next = l1 or l2
        return root.next
# @lc code=end

