#
# @lc app=leetcode.cn id=132 lang=python3
# @lcpr version=30202
#
# [132] 分割回文串 II
#

# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        result = []
        current = []
        dp = [[False]*n]*n
        def is_parlindome(substr):
            return substr==substr[::-1]
        def traceback(start:int):
            if start == n:
                result.append(current[:])
            for i in range(n):
                substr = s[start: i+1]
                if is_parlindome(substr):
                    current.append(substr)
                    traceback(i+1)
                    current.pop()
        traceback(0)
        return result

# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n
# @lcpr case=end

#

