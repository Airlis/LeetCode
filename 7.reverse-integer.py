#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        # [::-1] reverses a string
        if x < 0:
            rev = -1 * int(str(-1 * x)[::-1])
        else:
            rev = int(str(x)[::-1])
        if rev < -2 ** 31 or rev >= 2 ** 31:
            return 0
        else:
            return rev
# @lc code=end

