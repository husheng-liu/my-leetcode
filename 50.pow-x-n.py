#
# @lc app=leetcode.cn id=50 lang=python3
# @lcpr version=30111
#
# [50] Pow(x, n)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # if n< 0:
        #     return 1/self.myPow(x, -n)
        # # 由于存在最大递归深度，所以这里需要改下
        # # if n>0:

        # #     return self.myPow(x, n-1)*x
        # if n % 2 == 0:
        #     return self.myPow(x, n//2)* self.myPow(x, n//2)
        # else:
        #     return self.myPow(x,n//2) * self.myPow(x , n//2)* x
        # 由于递归存在最大深度和时间限制，改成了迭代 
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res

solution = Solution()

print(solution.myPow(2.0, 2))
            
# @lc code=end



#
# @lcpr case=start
# 2.00000\n10\n
# @lcpr case=end

# @lcpr case=start
# 2.10000\n3\n
# @lcpr case=end

# @lcpr case=start
# 2.00000\n-2\n
# @lcpr case=end

#

