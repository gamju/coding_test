# @before-stub-for-debug-begin
# from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (34.50%)
# Likes:    30424
# Dislikes: 2821
# Total Accepted:    3.5M
# Total Submissions: 10.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        # if 0 in sorted_nums:
        #     zero_loc = sorted_nums.index(0)
        # else:
        #     zero_loc = 0

        result_num_list = []
        result_sort_num_list = []
        
        for i in range(sorted_nums.__len__()):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            j = i+1
            k = sorted_nums.__len__() - 1
            while(j < k):
                sum = sorted_nums[i] +sorted_nums[j] + sorted_nums[k]
                if(sum > 0):
                    k = k - 1
                    continue
                elif(sum < 0):
                    j = j + 1
                else:
                    result_num_list.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j = j + 1
                    while sorted_nums[j] == sorted_nums[j-1] and j < k:
                        j = j+1
            
        return result_num_list


        
# @lc code=end

