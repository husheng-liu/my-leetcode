#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30113
#
# [136] 只出现一次的数字
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # tmp = []
        # for i in range(len(nums)):
        #   if nums[i] not in tmp:
        #     tmp.append(nums[i])
        #   else:
        #     tmp.remove(nums[i])

        # return tmp[0]
        # 这玩意只能靠记住了
        res = 0
        # 第二遍有方法了 0和任务数字异或都等于其自身，另外异或运算满足结合律，相同元素异或为0，最后剩下那个单个元素

        for num in nums:
            print(res, num)
            # 异或操作，相同为False,不同为True
            res = res^num
            print(res)
        return res
s = Solution()
print(s.singleNumber(nums = [0,1,2,2,1]))

# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

