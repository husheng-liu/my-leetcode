#
# @lc app=leetcode.cn id=384 lang=python3
# @lcpr version=30118
#
# [384] 打乱数组
#

from typing import List
import random

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tmp = list(nums)

    def reset(self) -> List[int]:
        return self.tmp

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)-1, 0, -1):
            j = random.randint(0,i)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums=[1,2,3,4,5])
# param_1 = obj.reset()
# print(param_1)
# param_2 = obj.shuffle()
# print(param_2)
# param_1 = obj.reset()
# print(param_1)
# @lc code=end



