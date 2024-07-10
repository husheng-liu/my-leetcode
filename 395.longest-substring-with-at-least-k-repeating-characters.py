#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30118
#
# [395] 至少有 K 个重复字符的最长子串
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

# 如果不存在这样的子字符串，则返回 0。
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        print("s",s)
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0)+1
        # 字串必须连续，所以不满足条件的地方可以直接分开（二分）
        for i, char in enumerate(s):
            # 连续通过的才能算作有效重复子串，所以不满足条件的地方就要分开探索了
            if char_count[char]<k:
                # 递归找到
                left = self.longestSubstring(s[:i],k)
                # print(left)
                right = self.longestSubstring(s[i+1:],k)
                
                return max(left, right)
        # 如果都满足条件
        print("len(s):", len(s))
        return len(s)
s = Solution()
print(s.longestSubstring(s = "ababbc", k = 3))



# @lc code=end



#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

