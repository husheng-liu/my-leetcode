#
# @lc app=leetcode.cn id=268 lang=python3
# @lcpr version=30118
#
# [268] 丢失的数字
#
# 输入：nums = [3,0,1]
# 输出：2

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    #     nums_set = set(nums)
    #     for i in range(len(nums)):
    #         if i not in nums_set:
    #             return i
    #     return len(nums)
        nums.sort()
        left = 0
        right = len(nums)-1
        # 如果左侧不少那么nums[mid]==mid,如果左侧少，那么nums[mid]>mid
        # 如果右侧少，那么nums[mid]==mid,所以这就是两个条件
        while left<=right:
            mid = (left+right)//2
            # 左侧不少，右侧少
            if mid ==nums[mid]:
                left = mid+1
            # 否则左侧少
            else:
                right = mid-1
        return left
    
            
                


s = Solution()
print(s.missingNumber([0,1]))

# @lc code=end



#
# @lcpr case=start
# [3,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [9,6,4,2,3,5,7,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

