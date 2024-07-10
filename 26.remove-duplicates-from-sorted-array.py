#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30111
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        cur_point = 0
        next_point = 1
        while next_point< len(nums):
            if nums[cur_point]==nums[next_point]:
                nums.remove(nums[cur_point])
            else:
                cur_point = next_point
                next_point += 1
        return len(nums)

solution = Solution()
print(solution.removeDuplicates([1,1,2]))
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

