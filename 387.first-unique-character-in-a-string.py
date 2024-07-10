#
# @lc app=leetcode.cn id=387 lang=python3
# @lcpr version=30118
#
# [387] 字符串中的第一个唯一字符
#
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
# 输入: s = "loveleetcode"
# 输出: 2
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
        print(d)
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
s = Solution()
print(s.firstUniqChar(s = "loveleetcode"))
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#

