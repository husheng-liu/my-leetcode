#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30116
#
# [215] 数组中的第K个最大元素
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5

# 521364  561324 564321
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 1 2 2 3 3 4 5 5 6
# 输出: 4

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import random 
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:

#         def quickselect(nums, left, right, k):
#             pivot_idx = partition(nums, left, right)
#             if pivot_idx == k:
#                 return nums[pivot_idx]
#             elif pivot_idx > k: 
#                 return quickselect(nums, left, pivot_idx-1, k)
#             else:
#                 return quickselect(nums, pivot_idx+1, right, k)

#         def partition(nums, left, right):
#             # 如果每次都是最右边，相当于全部都要遍历一遍
#             pivot = nums[right]
#             i = left - 1 
#             for j in range(left, right):
#                 if nums[j] <= pivot:
#                     i += 1
#                     nums[i], nums[j] = nums[j], nums[i]
#             nums[i+1], nums[right] = nums[right], nums[i+1]
#             return i+1

#         return quickselect(nums, 0, len(nums)-1, len(nums)-k)
# import random 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick(nums, l, r, k):
            if l >= r: return nums[l]
            x = nums[l + r >> 1]
            i, j = l - 1, r + 1
            while i < j:
                while True:
                    i += 1
                    if nums[i] <= x: break
                while True:
                    j -= 1
                    if nums[j] >= x: break
                if i < j: nums[i], nums[j] = nums[j], nums[i]
            if j - l + 1 >= k: 
                return quick(nums, l, j, k)
            else: 
                x = k - (j - l + 1)
                return quick(nums, j + 1, r, x)
        
        return quick(nums, 0, len(nums) - 1, k)

# class Solution:
#     def findKthLargest(self, nums, k):
#         def quick_select(nums, k):
#             # 随机选择基准数
#             pivot = random.choice(nums)
#             big, equal, small = [], [], []
#             # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
#             for num in nums:
#                 if num > pivot:
#                     big.append(num)
#                 elif num < pivot:
#                     small.append(num)
#                 else:
#                     equal.append(num)
#             if k <= len(big):
#                 # 第 k 大元素在 big 中，递归划分
#                 return quick_select(big, k)
#             if len(nums) - len(small) < k:
#                 # 第 k 大元素在 small 中，递归划分, 既然小，就找较大的
#                 return quick_select(small, k - len(nums) + len(small))
#             # 第 k 大元素在 equal 中，直接返回 pivot
#             return pivot
        
#         return quick_select(nums, k)
s = Solution()
print(s.findKthLargest([3,2,1,5,6,4], 3))

# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

