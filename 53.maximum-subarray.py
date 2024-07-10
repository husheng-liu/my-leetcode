#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30113
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # result = 0
        # for i in range(1, len(nums)+1):
        #     left = 0
        #     while left+i<=len(nums): 
        #         sum_sub = sum(nums[left:left+i])
        #         print(nums[left:left+i])
        #         if sum_sub > result:
        #             result= sum_sub
        #         left += 1
        # return result
        # 动态规划的解题思路：dp[i] 是以第i个元素结尾时的子数组的最大和
        # dp[i] 的更新规则（转移方程）当第i个元素时，,其最大子数组和是需要连续的，dp[i-i] 要么加上nums[i]，
        # 要么取nums[i]，不能保持dp[i-1],因为可选的子数组都是连续的，保持dp[i-1]意味着不连续。
        if not nums:
            return 0

        current_sum = max_sum = nums[0]

        for num in nums[1:]:
            # print("num:", num)
            # print("current_sum: ", current_sum)
            # print("current_sum+num: ", current_sum,"+",num)
            current_sum = max(num, current_sum + num)
            print("current_sum1: ", current_sum)
            # max_sum = max(max_sum, current_sum)
            # print("max_sum: ", max_sum)

        return max_sum
        # dp = [0 for _ in range(len(nums))]
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     # if dp[i-1]>0:
        #     #     dp[i] = dp[i-1]+nums[i]
        #     # else:
        #     #     dp[i] = nums[i]
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        # print(dp)
        return max(dp)

    

solution = Solution()
print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

