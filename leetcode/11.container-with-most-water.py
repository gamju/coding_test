#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        left = 0
        right = heights.__len__() - 1
        while(right > left):
            height = min(heights[left], heights[right])
            width = right - left
            water = width * height
            max_water = max(water, max_water)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        print(max_water)
        return max_water

        
# @lc code=end

    