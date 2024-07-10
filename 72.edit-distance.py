#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30203
#
# [72] 编辑距离
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 动态规划问题，1 定义dp[i][j]表示前面长度为i的字符串转化为n前面长度为j的字符串所需要的最小操作数
# 2 状态转移函数分为两种情况 1 两个字符串相同，2 两个字符串不同

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # mxn 
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # dp[0][j]表示word1 前0个变成word2前j个所需要的操作数，显然为j,同样的，
        # dp[i][0]表示word1 前i个变成word2前0个所需要的操作数，显然为i.
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        # dp[m][n] 即为所求，为了不出界，需要dp的维度为（m+1，n+1）
        # dp[i][j+1]表示word1的前i段变成转为word2 前j+1段
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # 对于word1的第i个字符 和word2 的第j个字符，如果两个字符一样，那么有转移函数
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 如果两个字符不同，需要在前一步的基础上加1，前一步到这一步有可能插入，删除或者替换
                    dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[m][n]
    
s = Solution()
print(s.minDistance("horse", "ros"))
        
# @lc code=end

#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

