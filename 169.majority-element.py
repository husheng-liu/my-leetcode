#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30116
#
# [169] 多数元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
# 时间复杂度o(n),空间复杂度o(1)
# 抵消方法，因为多数元素抵消后一定会保留下来

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate=num
            if num == candidate:
                count += 1  
            else:
                count -=1

        return candidate


# @lc code=end


class Solution:
    def majorityEle(self,nums):
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate==num:
                count +=1
            else:
                count -= 1
        return candidate
#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

