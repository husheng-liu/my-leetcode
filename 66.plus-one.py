#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=30113
#
# [66] 加一
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            # digits[i] += 1
            if digits[i]<9:
                digits[i] +=1
                return digits
            digits[i] = 0
        digits.insert(0,1)
        return digits


s = Solution()
print(s.plusOne(digits = [9,9,9,9]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

