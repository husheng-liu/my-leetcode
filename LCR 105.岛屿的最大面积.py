#
# @lc app=leetcode.cn id=LCR 105 lang=python3
# @lcpr version=30203
#
# [LCR 105] 岛屿的最大面积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(grid, cur_i,cur_j):
            if cur_i<0  or cur_j<0 or cur_i==len(grid) or cur_j==len(grid[0]) or grid[cur_i][cur_j] !=1:
                return 0
            grid[cur_i][cur_j] = 0
            ans = 1
            for di, dj in [[0, 1],[0,-1], [1,0], [-1,0]]:
                next_i = cur_i+di
                next_j = cur_j+dj
                ans +=dfs(grid, next_i, next_j)
            return ans

        ans = 0
        for i in range(m):
            for j in range(n):
                # if grid[i][j]==1:
                    # 探索（i，j)
                ans = max(dfs(grid, i, j), ans)
        return ans
# @lc code=end
# class Solution:
#     def dfs(self, grid, cur_i, cur_j) -> int:
#         if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
#             return 0
#         grid[cur_i][cur_j] = 0
#         ans = 1
#         for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
#             next_i, next_j = cur_i + di, cur_j + dj
#             ans += self.dfs(grid, next_i, next_j)
#         return ans

#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         ans = 0
#         for i, l in enumerate(grid):
#             for j, n in enumerate(l):
#                 ans = max(self.dfs(grid, i, j), ans)
#         return ans

# @lcpr case=start
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
print(solution.maxAreaOfIsland(grid))
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0,0,0,0,0]]\n
# @lcpr case=end

#

