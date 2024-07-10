#
# @lc app=leetcode.cn id=69 lang=python3
# @lcpr version=30113
#
# [69] x 的平方根 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 0, x
        
        while left <= right:
            mid = (left + right)//2
            # 夹逼的方式，调整左右指针
            if mid * mid <= x< (mid+1)*(mid+1):
                return mid
            if mid * mid >x:
                right = mid-1
            if mid * mid < x:
                left = mid + 1
s = Solution()
print(s.mySqrt(x=12))
            
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 8\n
# @lcpr case=end

#

