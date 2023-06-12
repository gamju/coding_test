#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(nums.__len__() - 1):
            for j in range(i+1,nums.__len__()):
                if nums[i] + nums[j] == target:
                    return [i,j]

        # print(nums)
        
# @lc code=end

