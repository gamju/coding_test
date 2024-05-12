#
# @lc app=leetcode id=12 lang=python3
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


