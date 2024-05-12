# @before-stub-for-debug-begin
from python3problem12 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (64.73%)
# Likes:    6949
# Dislikes: 5508
# Total Accepted:    1.3M
# Total Submissions: 2M
# Testcase Example:  '3749'
#
# Seven different symbols represent Roman numerals with the following
# values:
# 
# 
# 
# 
# Symbol
# Value
# 
# 
# 
# 
# I
# 1
# 
# 
# V
# 5
# 
# 
# X
# 10
# 
# 
# L
# 50
# 
# 
# C
# 100
# 
# 
# D
# 500
# 
# 
# M
# 1000
# 
# 
# 
# 
# Roman numerals are formed by appending the conversions of decimal place
# values from highest to lowest. Converting a decimal place value into a Roman
# numeral has the following rules:
# 
# 
# If the value does not start with 4 or 9, select the symbol of the maximal
# value that can be subtracted from the input, append that symbol to the
# result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one
# symbol subtracted from the following symbol, for example, 4 is 1 (I) less
# than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
# subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and
# 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times
# to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D)
# multiple times. If you need to append a symbol 4 times use the subtractive
# form.
# 
# 
# Given an integer, convert it to a Roman numeral.
# 
# 
# Example 1:
# 
# 
# Input: num = 3749
# 
# Output: "MMMDCCXLIX"
# 
# Explanation:
# 
# 
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
# ⁠700 = DCC as 500 (D) + 100 (C) + 100 (C)
# ⁠ 40 = XL as 10 (X) less of 50 (L)
# ⁠  9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on
# decimal places
# 
# 
# 
# Example 2:
# 
# 
# Input: num = 58
# 
# Output: "LVIII"
# 
# Explanation:
# 
# 
# 50 = L
# ⁠8 = VIII
# 
# 
# 
# Example 3:
# 
# 
# Input: num = 1994
# 
# Output: "MCMXCIV"
# 
# Explanation:
# 
# 
# 1000 = M
# ⁠900 = CM
# ⁠ 90 = XC
# ⁠  4 = IV
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 3999
# 
# 
#

# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_list = {1:'I', 5:'V', 10:'X', 50: 'L', 100:'C', 500:'D', 1000:'M'}
        value_list = sorted(list(str_list.keys()))
        print(value_list)
        num_to_str = str(num)
        num_len = num_to_str.__len__()
        result_roman = ""
        for i in range(num_len)[::-1]:
            cur_range = value_list[i*2 : i*2 + 3]
            print(i, cur_range)
            if i == 3:
                remain_num = int(num / 1000)
                num = num % 1000
            else:
                remain_num = int(num / cur_range[0])
                num = num % cur_range[0]
            if remain_num == 4:
                cur_roman = str_list[cur_range[0]] + str_list[cur_range[1]]
            elif remain_num == 9:
                cur_roman = str_list[cur_range[0]] + str_list[cur_range[2]]
            else:
                remain_5 = ''
                if remain_num > 4:
                    remain_5 = str_list[cur_range[1]]
                cur_roman = remain_5 + (remain_num%5)*str_list[cur_range[0]]
            result_roman += cur_roman
        return result_roman
# @lc code=end

