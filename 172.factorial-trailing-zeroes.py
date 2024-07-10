#
# @lc app=leetcode.cn id=172 lang=python3
# @lcpr version=30116
#
# [172] 阶乘后的零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros_count = 0
        while n >= 5:
            n //= 5
            zeros_count += n
        return zeros_count
    
s = Solution()
print(s.trailingZeroes(125))
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

