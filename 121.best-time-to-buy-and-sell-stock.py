#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30113
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 时间复杂度太高，超时
        # max_profit = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i, n):
        #         max_profit = max(prices[j]-prices[i],max_profit)
        # return max_profit
        max_profit = 0
        n = len(prices)
        min_price = prices[0]
        for i in range(n):
           # 遍历过程中固定最小价格，减少重复计算
           min_price = min( prices[i],min_price)
           # 只要没有找到最小价格，当前价格就会比前面的价格大
           max_profit = max(prices[i]-min_price, max_profit)
        return max_profit
s = Solution()
print(s.maxProfit(prices = [8,5,2,1,6,4]))
            
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

