#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30113
#
# [152] 乘积最大子数组
#
# nums = [2,3,-2,4]
# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [0]*(n+1)
        # 一种方式是通过找到乘积最大子数组，从而计算最大乘积
        # 另一种方式直接计算其中的乘积，找到最大的乘积

        max_product = nums[0]
        min_product = nums[0]
        result = max_product

        for i in range(1, n):
            tmp_max = max(max_product*nums[i], min_product*nums[i], nums[i])
            tmp_min = min(max_product*nums[i], min_product*nums[i], nums[i])
            max_product = tmp_max
            min_product = tmp_min
            result = max(result, max_product)
        return result

s = Solution()
print(s.maxProduct(nums = [-2,3,-4]))

# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#

