#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30118
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # # 用一套打平的索引是不能解决问题的,参考示例
        # if not matrix or not matrix[0]:
        #     return False
        # rows = len(matrix)
        # columns = len(matrix[0])
        # left = 0
        # right = rows*columns-1
        
        # while left<= right:
        #     mid = (left + right)//2
        #     row = mid//columns
        #     col = mid%columns
        #     if matrix[row][col] == target:
        #         return True
        #     elif matrix[row][col] > target:
        #         right = mid - 1
        #     else: 
        #         left = mid + 1
        #     print(left, right)
        # return False
    
    # def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        columns = len(matrix[0])

        row = 0
        col = columns - 1
        # 搜索的位置应该是一个位置比当前位置大，
        # 一个位置比当前位置小，所以一般选择角进行遍历
        # 虽然不用中分，但其实这种搜索路径也是二分
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False
            
# s = Solution()
# print(s.searchMatrix([[1,4],[2,5]], 2))
        
# @lc code=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#


            

        
# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

