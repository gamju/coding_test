#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        str_list = {1:'I', 5:'V', 10:'X', 100:'C', 500:'D', 1000:'M'}
        value_list = list(str_list.keys())
        M_count = int(num/1000)
        num = num%1000
        answer_list = []
        print(num)
        while(num):
            for idx in range(value_list.__len__()):
                if value_list[idx] > num:
                    num = num%value_list[idx-1]
                    print(num)
                    answer_list.append(str_list[value_list[idx-1]])
        return answer_list



        
# @lc code=end

