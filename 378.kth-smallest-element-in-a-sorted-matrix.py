#
# @lc app=leetcode.cn id=378 lang=python3
# @lcpr version=30118
#
# [378] 有序矩阵中第 K 小的元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import heapq
# 排序法空间复杂度为o（n2)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # def countlessequal(matrix, val):
        #     """在有序递增矩阵中，计算小于等于val 的元素个数
        #     """
        #     row,col = len(matrix), len(matrix[0])
        #     i, j = row-1,0
        #     count = 0
        #     while j<col and i>=0 :
        #         if matrix[i][j] <= val:
        #             count += i+1
        #             j += 1
        #         else:
        #             i -= 1
        #     return count
        # row = len(matrix)
        # col = len(matrix[0])
        # max_val, min_val = matrix[row-1][col-1], matrix[0][0]
        # while min_val<max_val:
        #     mid = (max_val+min_val)//2
        #     count = countlessequal(matrix, mid)
        #     print(count)
        #     if count<k:
        #         min_val = mid+1
        #     # 如果小于等于mid 的数量比k多，说明第k小元素在mid 左侧。
        #     # 不断夹逼，最终使得min_val 和max_val相等且等于kth smallest.
        #     elif count>=k:
        #         max_val = mid
        #     # 就算count=k，说明小于等于两者的个数相等，但是，返回的mid 是算出来的，不是数组原来的元素
        #     # else:
        #     #     return mid
        #     print(min_val, max_val)
        # return min_val 
# #         输入：matrix = [[1,5,9],
#                         [10,11,13],
#                         [12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
        def countlessequal(num)->int:
            row = len(matrix)
            col = len(matrix[0])
            count = 0
            j = 0
            while j< col and row>=0:
                if matrix[row-1][j] <= num:
                    count += row
                    j += 1
                else:
                    row -= 1
            return count
        
        row = len(matrix)
        col = len(matrix[0])
        max_val = matrix[row-1][col-1]
        min_val = matrix[0][0]
        while min_val<max_val:
            mid = (max_val+min_val)//2
            count = countlessequal(mid)
            if count<k:
                min_val = mid+1
            else:
                max_val = mid
        return min_val
# s = Solution()
# print(s.kthSmallest( [[1,5,9],[10,11,13],[12,13,15]], k=8))
# @lc code=end



#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

