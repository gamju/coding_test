#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (28.15%)
# Likes:    11971
# Dislikes: 2125
# Total Accepted:    952.3K
# Total Submissions: 3.4M
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# 
# 
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# 
# Example 1:
# 
# 
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
# by repeating 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = s.__len__()
        p_len = p.__len__()
        
        cnt = 0
        p_idx = 0
        for s_idx in range(s_len):
            cur_s = s[s_idx]

            if p_idx < p_len:
                cur_p = p[p_idx]
            else:
                return False
            
            if cur_p == ".":
                cur_p = cur_s
                prev_p = "."
                p_idx += 1
            elif cur_p == "*":
                cur_p = prev_p
                if cur_p == ".":
                    cur_p = cur_s
                    prev_p = "."
            else:
                prev_p = cur_p
                p_idx += 1
                
            if cur_p == cur_s:
                cnt+=1
                last_cnt = 1
            else:
                last_cnt = 0
                if cur_p == "*":
                    p_idx += 1
        
        print(cnt, last_cnt)
        if (cnt == s_len) and (last_cnt)== 1:
            return True
        else:
            return False
        # return 0
        
# @lc code=end

