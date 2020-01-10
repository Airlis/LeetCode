#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            if nums[left_index] == val:
                nums[left_index] = nums[right_index]
                right_index -= 1
            else:
                left_index += 1
        return left_index

# @lc code=end

