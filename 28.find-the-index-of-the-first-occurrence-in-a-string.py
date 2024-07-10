#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30111
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)
        result = -1
        while right<= len(haystack):
            if needle==haystack[left: right]:
                return left
            else:
                left += 1
                right += 1
        return result
solution = Solution()
print(solution.strStr(haystack = "a", needle = "a"))
# @lc code=end



#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#

