#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30113
#
# [139] 单词拆分
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import re


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
# dp[i]表示字段s[:i]可以由字典中单词组成。dp[len(s)]
# 截取字符串中的片段需要两个指针i,j 对于s[i:j]
# 判断是否位于字典，然后逐渐扩展s[i:j]到s[i+1:j],
# 所以j用于表示片段右侧，i表示遍历左侧到右侧每一个位置。


class Solution:
    def wordBreak(s, wordDict):
        n = len(s)
        dp = [False]*n
        dp[0]=True
        for j in range(n+1):
            for i in range(j):
                # 不满足的仍保持false(0,j)(1,j),(i,j),(j-1,j)
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    # 在这个范围内,如果存在就不再后续判断
                    break
        return dp[n]
        
s = Solution()
print(s.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

