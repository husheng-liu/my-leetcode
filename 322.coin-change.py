#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30118
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示金额为i是所需要的硬币最少数量
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                # 如果i-coin 小于0那么dp[i-coin]==0,最小的就会一直是1. 
                if coin<=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        print(dp)
        return dp[amount] if dp[amount]!=float('inf') else -1
s = Solution()
print(s.coinChange([1,2,5], 11))
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

