#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30111
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 选转= 转置+ 调换
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 转置
        
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        print(matrix)
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]
        print(matrix)
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        # # 翻转每一行
        # for i in range(n):
        #     for j in range(n // 2):
        #         matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        # print(matrix)
solution = Solution()
print(solution.rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

