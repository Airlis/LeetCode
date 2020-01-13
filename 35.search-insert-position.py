#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        if nums[-1] < target:
            index = len(nums)
        for i in range (len(nums)):
            if nums[i] >= target:
                index = i
                break
        return index

        # binary search!!!
        # l , r = 0, len(nums)-1
        # while l <= r:
        #     mid=(l+r)/2
        #     if nums[mid]== target:
        #         return mid
        #     if nums[mid] < target:
        #         l = mid+1
        #     else:
        #         r = mid-1
        # return l

# @lc code=end

