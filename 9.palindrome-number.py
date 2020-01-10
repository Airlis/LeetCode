#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # The first digit of the number cannot be 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        digits_left = x
        second_half = 0
        while digits_left > second_half:
            last_digit = digits_left % 10
            second_half = second_half * 10 + last_digit
            # // must be used to get a integer as solution
            digits_left = digits_left // 10

        # Second condition is for odd digits numbers, 
        # e.g. x = 121, then digits_left = 1, second_half = 12
        if digits_left == second_half or digits_left == second_half // 10:
            return True
        else:
            return False
# @lc code=end

