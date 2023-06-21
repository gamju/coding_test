#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = 1
        p_idx = 0
        for s_idx in range(s.__len__()):
            
            try:
                print(p_idx, p[p_idx], s[s_idx])
                if p[p_idx] == '*':
                    if p_idx + 1 >= p.__len__():
                        return 1
                    else:
                        if (p[p_idx + 1] == s[s_idx + 1]) or (p[p_idx + 1] == '.'):
                            p_idx += 1
                elif (p[p_idx] == s[s_idx]) or (p[p_idx] == '.'):
                    p_idx += 1
                    s_idx += 1

                elif p[p_idx] != s[s_idx]:
                    print(p_idx, p[p_idx], s[s_idx])
                    return -1
            except:
                print(p_idx, p_idx, s_idx)
                return False
        
        print(result)
        return result
        
# @lc code=end

