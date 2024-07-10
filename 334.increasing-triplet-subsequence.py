#
# @lc app=leetcode.cn id=334 lang=python3
# @lcpr version=30118
#
# [334] 递增的三元子序列
#

# 输入：nums = [2,1,5,0,4,6]
# 输出：true
# # 解释：三元组 (3, 4, 5) 
# 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 这里应该不是连续的子数列也可以
        # i = 0
        # n = len(nums)
        # while i<n-2:
        #     if nums[i]< nums[i+1]<nums[i+2]:
        #         return True
        #     else:
        #         i = i + 1
        # return False
        small = float('inf')
        mid = float('inf')
        print(len(nums))
        for num in nums:
            if num<=small:
                small = num
            elif num<=mid:
                mid = num
            else:
                return True
        return False
s = Solution()
print(s.increasingTriplet(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,5,0,4,6]\n
# @lcpr case=end

#

