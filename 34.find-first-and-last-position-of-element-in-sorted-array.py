#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30111
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 二分法：左边找和target 相等的第一个元素，右边找比target 大1 的第一个元素，然后索引减去 1
# 这样中间就是target 的索引，否则直接去找就会产生很多种情况，比较麻烦。
# 以下是直接法：
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = 0
#         right = len(nums)-1
#         start = -1
#         end = -1
#         while left <= right:
#             mid = (left+ right)//2
#             if nums[mid] == target:
#                 start = mid
#                 end = mid
#                 if len(nums)==1:
#                     return [start, end]
#                 elif len(nums)==2:
#                     if mid+1<len(nums):
#                         if nums[mid] == nums[mid+1]:
#                             end = mid+1
#                             mid = mid +1
#                             return [start, end]
#                         else:
#                             return [start, end] 
#                     else:
#                         return [start, end]
#                 else:
#                     while mid-1 > 0 and nums[mid]==nums[mid-1]:
#                         start = mid-1
#                         mid = mid-1
#                     mid = (left + right)//2
#                     if mid+1 <len(nums):
#                         while mid+1< len(nums) and nums[mid] == nums[mid+1]:
#                             end = mid+1
#                             mid = mid +1
#                         return [start, end]
#                     else:
#                         return [start, end]
#             elif target < nums[mid]:
#                 right = mid-1

#             else:
#                 left = mid + 1

#         return [start, end]
# solution = Solution()
# print(solution.searchRange([3,3,3], 3))
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        elif len(nums)==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        elif len(nums)>1:  
            start = self.findfirstequal(nums, target)
            end = self.findlastequal(nums, target)
            return [start, end]

    def findfirstequal(self, nums, target):
        left = 0
        right = len(nums)-1
        # 指针重叠
        result = -1
        # [5,7,7,8,8,10] 8
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                result = mid
                right = mid-1
            elif nums[mid]< target:
                left = mid+1
            else:
                right = mid - 1
        return result
    
    def findlastequal(self, nums, target):
        left = 0
        right = len(nums)-1
        # 指针重叠
        result = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                result = mid
                left = mid+1
            elif nums[mid]< target:
                left = mid+1
            else:
                right = mid - 1
        return result


s = Solution()
print(s.searchRange([5,7,7,8,8,10], 8))









# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         # if not nums:
#         #     return [-1, -1]
#         # elif len(nums)==1:
#         #     if nums[0]==target:
#         #         return [0,0]
#         #     else:
#         #         return [-1, -1]
#         # elif len(nums)>1:
#         #     start = self.findFirstGreaterEqual(nums, target)
#         #     end = self.findFirstGreaterEqual(nums, target + 1)-1
#         #     print(start, end)
#         #     if start <= end:
#         #         return [start, end]
#         #     else:
#         #         return [-1, -1]
#         start = self.findFirstEqual(nums, target)
#         end = self.findLastEqual(nums, target)
#         return [start, end]
        
#     def findFirstEqual(self, nums, target):
#         left = 0
#         right = len(nums)-1
#         result = -1
#         while left<=right:
#             mid = (left+right)//2
#             # 找到如果不直接返回，可以继续找到第一个
#             if nums[mid] == target:
#                 result = mid
#                 right = mid-1
#             elif target< nums[mid]:
#                 right = mid-1
#             else:
#                 left = mid + 1
#         print(result)
#         return result
#     def findLastEqual(self, nums, target):
#         left = 0
#         right = len(nums)-1
#         result = -1
#         while left<=right:
#             mid = (left+right)//2
#             # 找到如果不直接返回，可以继续找到第一个
#             if nums[mid] == target:
#                 result = mid
#                 left = mid+1
#             elif target< nums[mid]:
#                 right = mid-1
#             else:
#                 left = mid + 1
#         print(result)
#         return result
# solution = Solution()
# print(solution.searchRange([11,12], 13))
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

