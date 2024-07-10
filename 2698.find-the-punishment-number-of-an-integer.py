#
# @lc app=leetcode.cn id=2698 lang=python3
# @lcpr version=30102
#
# [2698] 求一个整数的惩罚数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def check(self, i:int):
        def dfs(s, cur_sum):
            if not s:
                return cur_sum==i
            return any(dfs(s[j:], cur_sum+int(s[:j])) for j in range(1, len(s)+1))
        return dfs(str(i*i), 0)
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            if self.check(i):
                ans += i * i
        return ans
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 37\n
# @lcpr case=end

#

