#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        needle_size = len(needle)
        for i in range(len(haystack) - needle_size + 1):
            # only iterates until diff between haystack and needle
            for j in range (needle_size):
                # terminate when mismatching
                if haystack[i + j] != needle[j]:
                    break
                # finish when chars in needle are all checked
                if j == needle_size - 1:
                    return i

            # Another way in python:
            # if haystack[i:i + needle_size] == needle:
            #     return i
        return -1
            
# @lc code=end

