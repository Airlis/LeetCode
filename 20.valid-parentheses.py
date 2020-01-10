#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # In python, list can be used as a stack
        stack = []
        # Avoid using if statements for close brackets
        bracket_dict = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in bracket_dict:
                if len(stack) == 0:
                    return False
                bracket = stack.pop()
                if bracket != bracket_dict[char]:
                    return False
            else:
                stack.append(char)
        if len(stack) != 0:
            return False
        return True
            

# @lc code=end

