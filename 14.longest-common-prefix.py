#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs) == 0:
            return prefix
        first_word = strs[0]
        for i in range(0, len(first_word)):
            current_char = first_word[i]
            for j in range(1, len(strs)):
                current_word = strs[j]
                if len(current_word) <= i:
                    return prefix
                if current_word[i] != current_char:
                    return prefix
            prefix += current_char
        return prefix
# @lc code=end

