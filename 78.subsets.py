#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30113
#
# [78] 子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current = []
        self.backtrack(nums, 0, current, subsets)
        return subsets
    
    def backtrack(self, nums, start, current, subsets):
        subsets.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            print(subsets)
            print(i)
            self.backtrack(nums, i+1, current, subsets)
            print("pop:", current.pop())
            
s = Solution()
print(s.subsets([1,2,3]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

