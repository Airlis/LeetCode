#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        s = s.replace('IV', 'IIII')
        s = s.replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX')
        s = s.replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC')
        s = s.replace('CM', 'DCCCC')

        for digit in s:
            if digit == 'I':
                result += 1
            elif digit == 'V':
                result += 5
            elif digit == 'X':
                result += 10
            elif digit == 'L':
                result += 50
            elif digit == 'C':
                result += 100
            elif digit == 'D':
                result += 500
            elif digit == 'M':
                result += 1000
                
        return result

# @lc code=end

