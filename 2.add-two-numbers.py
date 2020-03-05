#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        result_tail = dummy
        carry = 0

        while l1 or l2 or carry:
            first_digit = (l1.val if l1 else 0)
            second_digit= (l2.val if l2 else 0)
            digit = int((first_digit + second_digit + carry) % 10)
            carry = int((first_digit + second_digit + carry) / 10)

            result_tail.next = ListNode(digit)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        
        return dummy.next

# @lc code=end

