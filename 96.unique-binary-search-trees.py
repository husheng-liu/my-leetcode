#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30113
#
# [96] 不同的二叉搜索树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # 从顶向底思考解法，从底到顶实现算法
        if n<2:
            return 1 
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        # 逐渐累积到n
        for i in range(2, n+1):
            # 节点数为i时，dp[i]的值
            # 要算出dp[i],必须要遍历每个根节点，
            # 因为dp[i] = dp[0]*dp[i-1]+dp[1]*dp[i-2]+...+dp[j-1]*dp[i-j]+...+dp[i-1]dp[0]
            for j in range(1, i+1):
                # 状态转移方程
                dp[i] += dp[i-j]*dp[j-1]#右子树*左子树
                print(dp)
        print(dp)
        return dp[n]
s = Solution()
print(s.numTrees(2))
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

