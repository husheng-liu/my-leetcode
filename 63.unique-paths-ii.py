#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30204
#
# [63] 不同路径 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 特殊形况需要考虑， 起点，终点， 单一元素等
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        if obstacleGrid==[[0]]:
            return 1
        dp = [[0]*n for _ in range(m)]
        for i in range(1, m):
            if obstacleGrid[i-1][0] ==0:
                dp[i][0] = 1 
            # 一旦边界有阻碍，那么后面全部为0, dp[i][j]表示到达(i,j)的路径
            else:
                break
        for j in range(1, n):
            if obstacleGrid[0][j-1] ==0:
                dp[0][j] = 1
            else:
                break
        print(dp)
     
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
                    dp[i][j] = 0 
                elif obstacleGrid[i-1][j] == 1:
                    dp[i][j] = dp[i][j-1]
                elif obstacleGrid[i][j-1] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]+dp[i-1][j]
        print(dp)
        return dp[m-1][n-1]
                
# @lc code=end

# @lcpr case=start
obstaclegrid =[[0,1,0,0,0],
               [1,0,0,0,0],
               [0,0,0,0,0],
               [0,0,0,0,0]]

s = Solution()
print(s.uniquePathsWithObstacles(obstaclegrid))
# @lcpr case=end

# @lcpr case=start
# [[0,1],
#  [0,0]]\n
# @lcpr case=end

#

