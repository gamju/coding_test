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
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a
# previous valid character to match.

# @lc code=start
class Solution:
    #중복 패턴 삭제 *a*a*a --> *a
    def zip_pattern(self, pattern):
        split_pattern = pattern.split("*")
        zipped_pattern = ""
        cur_pattern = ""
        for i in split_pattern[:-1]:
            print(i, cur_pattern)
            if i.__len__() > 2:
                cur_pattern = i[-1:]
                zipped_pattern += i + "*"
            elif i.__len__() == 0:
                break
            else:
                if i == cur_pattern:
                    continue
                else:
                    cur_pattern = i
                    zipped_pattern += i + "*"
        zipped_pattern += split_pattern[-1]
        return zipped_pattern
                

            

    def isMatch(self, s: str, p: str) -> bool:
        if p.find("*") > -1:
            p = self.zip_pattern(p)
        print(p)
        def rec(ss: str, pp: str) -> bool:
            # print(ss, pp)
            if ss.__len__() == 0 and pp.__len__() == 0:     
                # print(3)           
                return True            
            if pp.__len__() == 0 :           
                # print(4)
                return False
            
            cur_comp = bool(ss) and pp[0] in {ss[0], '.'}
            if pp.__len__() > 1 and pp[1] == "*":
                return rec(ss, pp[2:]) or cur_comp and rec(ss[1:], pp)
            else:
                # print(2)
                return cur_comp and rec(ss[1:], pp[1:])
        return rec(s,p)


# @lc code=end

