#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30113
#
# [122] 买卖股票的最佳时机 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # 只考虑局部最优，不考虑全局最优，贪心
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0:
                max_profit += diff
        
        return max_profit
    
    
       
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
                
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

