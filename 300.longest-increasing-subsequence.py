#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30118
#
# [300] 最长递增子序列
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 表示以num[i]结尾的列表的最长递增子序列
        n = len(nums)
        dp = [1]*n
        for i in range(1, n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)
    
s = Solution()
print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

