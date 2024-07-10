#
# @lc app=leetcode.cn id=130 lang=python3
# @lcpr version=30113
#
# [130] 被围绕的区域
#


# @lcpr-template-start

# @lcpr-template-end
from typing import List

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs
        m = len(board)
        n = len(board[0])
        def dfs(i,j):
            # i是行数，j是列数，行数不能小于0，不能大于等于m,j是列数，列数不能小于0，不能大于等于n
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != "O":
                return 
            board[i][j] = '#'
            # 查看board[i][j]周围是否为'O'
            dfs(i, j-1)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i+1, j)

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
s = Solution()
# 示例用法
board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]
# 和包围的岛屿不同
print(s.solve(board=board))
for row in board:
    print(row)
# @lc code=end



#
# @lcpr case=start
# [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]\n
# @lcpr case=end

# @lcpr case=start
# [["X"]]\n
# @lcpr case=end

#

