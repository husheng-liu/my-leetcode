#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30116
#
# [189] 轮转数组
#

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 整体反转，然后以k为分界线，左右翻转，这样左右部分都保持原来的顺序，但是位置翻转 
        def reverse(arr, start, end):
            while start< end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        k = k%len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
# s = Solution()
# nums = [1,2,3,4,5,6,7]
# s.rotate(nums, k = 3)
# print(nums)

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#

