#
# @lc app=leetcode.cn id=91 lang=python3
# @lcpr version=30113
#
# [91] 解码方法
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[n]是长度为n的字符串的解析方法总数
        #　索引要达到ｎ
        dp = [0] * (n+1)
        # dp[0]存放n=1
        dp[0] = 1
        if s[0] == "0":
            return 0
        dp[1] = 1
        # i 表示长度i的字符串
        for i in range(2, n+1):
            # 分以下两种情况进行汇总
            # s[i] 单独解码
            if s[i-1] !="0":
                dp[i] = dp[i] + dp[i-1]
            # s[i-2: i]合并解码
            if 10<=int(s[i-2:i])<=26:
                dp[i] = dp[i]+ dp[i-2]
        return dp[n]

s = Solution()
print(s.numDecodings("11106"))
        
# @lc code=end



#
# @lcpr case=start
# "12"\n
# @lcpr case=end

# @lcpr case=start
# "226"\n
# @lcpr case=end

# @lcpr case=start
# "06"\n
# @lcpr case=end

#

