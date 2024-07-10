#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30111
#
# [7] 整数反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            result = x[0]+x[1:][::-1]
        elif x[-1] == "0" and len(x)>1:
            result = x[:-1][::-1]
        elif x == "0":
            result = x
        else:
            result = x[::-1]
        result = int(result)
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
    
solution = Solution()
print(solution.reverse(0))
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

