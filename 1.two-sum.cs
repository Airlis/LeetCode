/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 */

// @lc code=start
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        int[] result = new int[2];
        for (int i = 0; i < nums.Length; i++)
        {
            if (dict.ContainsKey(target - nums[i]) )
            {
                result[0] = i;
                result[1] = dict[(target - nums[i])];
                break;
            }
            // Add the new elements to the dict here
            // to avoid the case:
            // (target - nums[i]) = nums[i]
            // e.g. nums[0] = 3, target = 3
            // If convert nums to dict first, the algorithm
            // will return (0, 0)
            if (!dict.ContainsKey(nums[i]))
            {
                dict.Add(nums[i], i);
            }
        }
        return result;
        
    }
}
// @lc code=end

