#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30117
#
# [238] 除自身以外数组的乘积
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 1 2 3 4
# 1 1 1 1
# 前缀积 1 1 2 6
# 后缀积 24 12 4 1 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        for i in range(1, n):
            prefix_product[i] = prefix_product[i-1] * nums[i-1]
        print(prefix_product)
        suffix_product = [1] * n 
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i+1]
        print(suffix_product)
        result = []
        for i in range(n):
            product_exceptself = prefix_product[i] * suffix_product[i]
            result.append(product_exceptself)
        return result 
        # 优化空间复杂度

        # 计算前缀乘积，并将结果存储在输入数组中
        n = len(nums)
        result = [0] * n

        # 计算前缀乘积
        prefix_product = 1
        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]
        print(prefix_product)
        print(result) 
        # 计算后缀乘积，并与前缀乘积相乘
        suffix_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        print(suffix_product) 
        return result
        # prefix_product = 1
        # for i in range(n):
        #     nums[i] , prefix_product  = prefix_product, prefix_product * nums[i]
        # suffix_product = 1
        # for i in range(n-1, -1, -1):
        #     nums[i], suffix_product  = nums[i] * suffix_product , suffix_product * nums[i]
        # return nums
s = Solution()
print(s.productExceptSelf([1,2,3,4]))

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

