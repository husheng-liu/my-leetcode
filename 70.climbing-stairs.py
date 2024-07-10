#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30113
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
      
        if n ==1:
            return 1
        if n == 2:
            return 2

        # 第n级台阶的方法是由最后一步爬两个台阶和爬一个台阶的方法组成的。
        # 这其实和机器人只能向右或者向下行走是一样的。
        else:
            dp[0] = 1
            dp[1] = 2
            for i in range(2, n):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[n-1]
    
s = Solution()
print(s.climbStairs(1))
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

