#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30116
#
# [198] 打家劫舍
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# dp[i]是 偷窃到第i家所获得的最高金额，第i家可以选择偷或者不偷。
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+ nums[i], dp[i-1])
        return dp[n-1]
    
s = Solution()
print(s.rob([1,2,3,4]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

