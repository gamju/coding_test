#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (42.78%)
# Likes:    17258
# Dislikes: 4499
# Total Accepted:    3.3M
# Total Submissions: 7.8M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# 
# Example 1:
# 
# 
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def find_prefix(self, short_str, long_str):
        short_str_len = short_str.__len__()
        result_prefix = ""
        for cut_loc in range(short_str_len):
            if result_prefix.__len__() > short_str_len - cut_loc:
                break
            # for start_idx in range(cut_loc + 1):
            cur_prefix_str = short_str[:short_str_len - cut_loc]
            if long_str.find(cur_prefix_str) == 0:
                result_prefix = cur_prefix_str
                break
        return result_prefix
                    

        
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sorted_strs = sorted(strs)
        cur_prefix = sorted_strs[0]
        for idx_str in sorted_strs[1:]:
            if cur_prefix.__len__() > idx_str.__len__():
                cur_prefix = self.find_prefix(idx_str, cur_prefix)
            else:
                cur_prefix = self.find_prefix(cur_prefix, idx_str)

        return cur_prefix

        
# @lc code=end

