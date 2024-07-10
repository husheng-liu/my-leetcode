#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30111
#
# [33] 搜索旋转排序数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 首尾指针, 循环终止条件是首小于尾
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1
#         while left<= right:
#             mid = (right + left)//2
#             print(left, mid, right)
#             if nums[mid]== target:
#                 return mid
#             elif nums[left] <= nums[mid]:
#                 if nums[left]<= target <= nums[mid]:
#                     right = mid-1
#                 else:
#                     left = mid+1
#             else:
#                 print(mid, right)
#                 if nums[mid]<= target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid-1
#         return -1

# solution = Solution()
# print(solution.search([3,1], target=1))
class Solution:
    def search(self, nums, target):
        left = 0
        n = len(nums)
        right = n-1
        # 这样的nums元素排列有一个特点，就是按照数字大小拍成两端，不会存在反向排列
        while left <= right:
            mid = (left+ right)//2
            if nums[mid] == target:
                return mid
            # 2456701
            # 当len(nums)==2,left 和mid 会重合
            elif nums[left]<= nums[mid]:
                # 这一段单减
                if nums[left]<= target<=nums[mid]:
                    right = mid-1
                # 这一段不单调，指针移动后进行下一个循环
                else:
                    left = mid + 1
            # 5670124
            else:
                # 这种情况下nums[mid] 一定小于nums[right],这一段单增
                if nums[mid]<= target<= nums[right]:
                    left = mid + 1
                # 这一段不单调，指针移动后进行下一个循环
                else:
                    right = mid -1
        return -1 
s = Solution()
print(s.search([3, 1], 1)) 
# @lc code=end



# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

