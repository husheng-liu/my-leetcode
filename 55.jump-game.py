#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30113
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_pos = 0
        for i in range(n):
            #因为index=0的位置是0，所以你无法移动， 说明此时陷入到0的位置
            # [0, 1,2,1,4]
            # [1, 0, 2, 1, 4]
            if i> max_pos:
                return False
            # 贪心算法，不管你到那一步，都应该选择最远的,最远的意味着你可以选择在这个范围以内的任何位置
            max_pos = max(i+nums[i], max_pos)
            if max_pos>=n-1:
                return True
        return False
    
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

