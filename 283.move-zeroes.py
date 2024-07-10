#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30118
#
# [283] 移动零

# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # left = 0
        # right = n-1
        # while left< right:
        #     if nums[left]==0 and nums[right]==0:
        #         right -=1 
        #     elif nums[left]==0 and nums[right]!= 0:
        #         nums[left], nums[right] = nums[right],nums[left]
        #         left += 1
        #         right -= 1
        #     elif nums[left] !=0 and nums[right]==0:
        #         left += 1
        #         right -= 1
        #     else:
        #         left += 1

        # return nums
        # count = 0 
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         nums.pop(i)
        #         count +=1
        # for i in range(count):
        #     nums.append(0)
        # return nums
        # [0,1,0,3,12]
        # 1, 1 0 3 12 
        # 1 3 0 3 12
        # 1 3 12 3 12
        left = 0
        right = 0
        n = len(nums)
        while right< n:
            if nums[right] != 0:
                nums[left] = nums[right] 
                left += 1
            right += 1
        while left< n:
            nums[left]=0
            left += 1
        return nums
s = Solution()
print(s.moveZeroes([0,0, 1]))
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

