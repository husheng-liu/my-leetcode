#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30118
#
# [279] 完全平方数
#

# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i]是 表示和为i的完全平方数的最少数量，
        # 找到dp[i]的等式方程至关重要
        # dp[i]等于dp[i-j*j] + 1, 但是dp[i-j*j]的j*j要<= i，
        # 小于的话属于正常递推，等于是就正好是一个完全平方数，
        # 所以要考虑这里面的全部情况，所以加上循环
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            # print("i: ", i)
            for j in range(1, int(i**0.5)+1): 
                # print("j: ", j)
                # dp[i]
                dp[i] = min(dp[i], dp[i-j*j]+1)
                # print(dp[i])
        return dp[n]
# s = Solution()
# print(s.numSquares(35))
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

