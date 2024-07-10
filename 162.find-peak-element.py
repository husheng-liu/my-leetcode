#
# @lc app=leetcode.cn id=162 lang=python3
# @lcpr version=30116
#
# [162] 寻找峰值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# nums = [1,2,1,3,5,6,4]
# 重要假设，边缘元素为负无穷
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while left< right:
            mid = (left+right)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            # 峰值一定在右侧
            elif nums[mid]< nums[mid+1]:
                left = mid+1
            else: 
                right = mid-1
           
        return left
    
nums = [1, 2, 3, 4]
s = Solution()
peak_index = s.findPeakElement(nums)
peak_value = nums[peak_index]
print("峰值的索引：", peak_index)
print("峰值的数值：", peak_value)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,5,6,4]\n
# @lcpr case=end

#

