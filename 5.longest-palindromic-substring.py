#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30111
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 动态规划，一般用一个二维数组来存放
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0
        dp = [[False]*n for _ in range(n)]
        # 长度为 1 的字串
        for i in range(n):
            dp[i][i] = True
        print(dp)
        # 不同长度的片段
        # length 最小为2，包含头尾，最长为n
        for length in range(2, n+1):
            # i， j 是 不同长度片段的两端指针
            # i 作为头,加上后面的，不能使得尾指针超出
            # i 最大:比如n=5,length=2,i最大5-2=3，
            # 但是range不包含3，所以应该+1
            for i in range(n-length+1):
                # j应该和i组成length 的长度，比如length=2,i=0,j应该是1，
                # 所以j=0+2-1
                j = i+ length-1
                # 如果两端相同，那么
                print(i, j)
                if s[i]==s[j]:
                    # 头尾相等的情况下，长度小于等于3，
                    # 或掐头去尾之后是回文串，那么这一段也是回文串
                    if length<=3 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if max_len<length:
                            max_len = length
                            start = i
        return s[start:start+max_len]

# @lc code=end
s = Solution()
print(s.longestPalindrome(s="babad"))


#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

