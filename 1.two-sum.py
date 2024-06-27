#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {} 
        for i in range(len(nums)):
            another = target - nums[i]
            if another not in dic:
                dic[nums[i]] = i
            else:
                return [i, dic[another]]
        
# @lc code=end

