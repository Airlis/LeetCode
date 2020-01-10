#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow_pointer = 0
        # fast_pointer iterates from the second int to the end
        for fast_pointer in range (1, len(nums)):
            # if duplicate ends, replace the next index of unique part
            if nums[fast_pointer] != nums[slow_pointer]:
                slow_pointer += 1
                nums[slow_pointer] = nums[fast_pointer]
        return slow_pointer + 1
# @lc code=end

