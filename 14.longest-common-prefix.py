#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30111
#
# [14] 最长公共前缀


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        if not strs:
            return result
        if len(strs)==1:
            result = strs[0]
        else:
            
            sign = list(strs[0])
            for i in range(len(sign)):
                flag = False
                for s in strs[1:]:
                    if i < len(s):
                        if s[i]==sign[i]:
                            flag = True
                        else:
                            return result
                    else:
                        return result
                if flag:
                    result+=sign[i]
                else:
                    break

        return result
    
solution = Solution()
print(solution.longestCommonPrefix(["c","acc","ccc"]))
            
# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

