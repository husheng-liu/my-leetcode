#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30113
#
# [125] 验证回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s)-1
        while left< right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
s = Solution()
print(s.isPalindrome(s = "race a car"))
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#

