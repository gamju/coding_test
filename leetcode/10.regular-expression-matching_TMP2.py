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
        return True
        # def rec(ss: str, pp: str) -> bool:            
        #     if not pp and not ss:                
        #         return True            
        #     if not pp :                
        #         return False            
        #     ppLen = len(pp)            
        #     ssLen = len(ss)            
        #     if ppLen > 1 and pp[1] == '*':                
        #         if rec(ss, pp[2:]) == True:                    
        #             return True                
        #         if ssLen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
        #             return rec(ss[1:], pp)
        #     else:
        #         if ssLen > 0 and (ss[0] == pp[0] or pp[0] == '.'):
        #             return rec(ss[1:], pp[1:])
        #     return False
        # return rec(s, p)
        # return 1


# @lc code=end

