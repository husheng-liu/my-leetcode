#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30111
#
# [509] 斐波那契数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1)+self.fib(n-2)

solution = Solution()
print(solution.fib(6))
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

