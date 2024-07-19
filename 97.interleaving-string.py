#
# @lc app=leetcode.cn id=97 lang=python3
# @lcpr version=30204
#
# [97] 交错字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 先考虑简单情况 ab cd  acbd
        # i,j 分别为s1和s2的前面的几个，
        #
        # dp[i][j]表示s1前i个,s2的前j个，能否交错构成s3[i+j]个。dp[0][0] = 1
        # 求dp[m1][m2]
        # 转移方程：
        m, n, d = len(s1), len(s2), len(s3)
        if d != m+n:
            return False
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            if s3[i-1] == s1[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n+1):
            # 当前相等的同时，前面还要有继承的关系，前面能构成，后面才能持续构成
            if s3[j-1] == s2[j-1]:
                dp[0][j] = dp[0][j-1]  
        for i in range(1, m+1): 
            for j in range(1,n+1):
                if (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[-1][-1]
# @lc code=end
# @lcpr case=start
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s = Solution()
print(s.isInterleave(s1,s2,s3))
# @lcpr case=end

# @lcpr case=start
# "aabcc"\n"dbbca"\n"aadbbbaccc"\n
# @lcpr case=end

# @lcpr case=start
# ""\n""\n""\n
# @lcpr case=end

#

