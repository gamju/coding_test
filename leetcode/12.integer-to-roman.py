#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        str_list = {1:'I', 5:'V', 10:'X', 50: 'L', 100:'C', 500:'D', 1000:'M'}
        value_list = list(str_list.keys())
        for idx, value in range(value_list.__len__() - 1, 1):
            remain_num = num / value
            num = num % value
            # 몫이 4,9 그 이외
            if remain_num == 0:
                continue
            if remain_num == 4:
                
            elif remain_num == 9:
            else:


                 

        return answer_list



        
# @lc code=end

