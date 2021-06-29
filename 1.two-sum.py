# @before-stub-for-debug-begin
from python3problem1 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            numSubtract = target - nums[i]
            if numSubtract in numDict:
                return [i, numDict.get(numSubtract)]
            else:
                numDict[nums[i]] = i

# @lc code=end
