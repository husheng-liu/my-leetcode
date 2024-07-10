#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30118
#
# [344] 反转字符串
#
# 输入：s = ["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid = n//2
        for i in range(mid):
            s[i], s[n-i-1] = s[n-i-1], s[i]

        
    
s = Solution()
a = ["H","a","n","n","a","h"]
s.reverseString(s=a)
print(a)

# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

