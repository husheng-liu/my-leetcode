#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30113
#
# [62] 不同路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]表示机器人到达第i行第j列的路径数
        dp = [[0]*n for _ in range(m)]
        # dp[0][0]为1 相当于默认规定
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = 1
        for j in range(1, n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
s = Solution()
print(s.uniquePaths(m=3, n=2))
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#

