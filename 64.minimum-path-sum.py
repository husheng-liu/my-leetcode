#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i]表示第i步的最小路径和，对于mxn 的方格，其总共需要走m+n-1步，
        # 对于dp[i]的转移方程等于dp[i-1]+grip[i-1][j] or dp[i-1]+grip[i][j-1]的最大值
        # dp[i][j]表示走到（i，j)时的最小路径和

        m = len(grid)
        n = len(grid[0])
        
        # dp = [[1,4,5],
        #       [2,7,6],
        #       [6,8,7]]
        dp = [[0] *n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        print(dp)
        return dp[m-1][n-1]
# @lc code=end
#
# @lcpr case=start
s = Solution()
grid= [
 [1,3,1],
 [1,5,1],
 [4,2,1]
 ]
print(s.minPathSum(grid))
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#

