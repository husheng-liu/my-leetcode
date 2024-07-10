#
# @lc app=leetcode.cn id=326 lang=python3
# @lcpr version=30118
#
# [326] 3 的幂
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n<=0:
        #     return False

        # while n != 1:
        #     if n % 3 != 0:
        #         return False
        #     n = n//3
        # return True
        if n<=0:
            return False
        if n ==1:
            return True
        if n % 3 != 0:
            return False

        return self.isPowerOfThree(n//3) 
     
    
    
s = Solution()
print(s.isPowerOfThree(0))
# @lc code=end



#
# @lcpr case=start
# 27\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 45\n
# @lcpr case=end

#

