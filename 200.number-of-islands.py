#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30116
#
# [200] 岛屿数量
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3#


# @lcpr-template-start

# @lcpr-template-end
from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != "1":
                return 
            grid[i][j] = "0"
            # 探索给定位置的左右上下，根据边界找出范围.
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i+1, j)
 
        count = 0
        for i in range(m):
            for j in range(n):
                #　如果是１,只要是1，就会存在岛屿，仅在需要探索是否成片，
                # 将成片的范围改成0，
                # 然后这一片就不会再被判断。之后判断其他位置的1.
                if grid[i][j]== "1":
                    count+=1
                    # print(grid)
                    dfs(i,j)
        return count


class solution:
    def numIslands(grid):
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            area = 1
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] !=1:
                return
            else:
                area +=1
                grid[i][j] = 0
            for x, y in [[0,-1],[0, 1], [-1,0], [1,0]]:
                dfs(i+x, j+y)
            # dfs(i-1,j)
            # dfs(i+1, j)
            # dfs(i, j-1)
            # dfs(i, j+1)
             
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count +=1
                    # 探索（i，j)
                    dfs(i, j)
        return count
s = Solution()
print(s.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))
# @lc code=end



#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#

