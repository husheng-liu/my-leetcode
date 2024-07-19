#
# @lc app=leetcode.cn id=120 lang=python3
# @lcpr version=30204
#
# [120] 三角形最小路径和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        # dp[i]表示三角形第i层的最小和
        # dp[i] 等于dp[i-1]+i层的某个值traingle[i][j],j由i-1层的元素决定
        # # 贪心算法是不对的，因为这是局部最优，恰好不等于全局最优
        # m = len(triangle)
        # dp = [0]*m
        # dp[0] = triangle[0][0]
        # j = 0
        # for i in range(1, m):
        #     if dp[i-1]+triangle[i][j]>dp[i-1]+triangle[i][j+1]:
        #         j = j+1
        #     dp[i] =dp[i-1]+triangle[i][j]

        # return dp[m-1]
        # dp[i][j]表示到达三角形[i,j]位置的最小路径和
        #转移方程dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        m = len(triangle)
        dp = [[0]*len(triangle[i]) for i in range(m)]
        dp[0] = triangle[0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+triangle[i][0]
            dp[i][-1] = dp[i-1][-1]+triangle[i][-1]
        print(dp)
        for i in range(2, m):
            # dp每一层的0，-1都不用计算了
            for j in range(1, len(triangle[i])-1):
                print(i, j)
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[m-1])
    
    def minimumTotal(self,triangle):
        m = len(triangle)
        # 这个最小路径，从上到下和从下向上,都是一样的
        # 从倒数第二层开始,假设m=4, 2，1，0
        for i in range(m-2,-1, -1):
            # i+1 表示i层的元素数量
            for j in range(i+1):
                triangle[i][j]+= min(triangle[i+1][j],triangle[i+1][j+1])
            # print(triangle)
        return triangle[0][0] 
# @lc code=end
triangle = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
# @lcpr case=start
# triangle= [[-1],[2,3],[1,-1,-3]]
s = Solution()
print(s.minimumTotal1(triangle))

# @lcpr case=end

# @lcpr case=start
# [[-10]]\n
# @lcpr case=end

#

