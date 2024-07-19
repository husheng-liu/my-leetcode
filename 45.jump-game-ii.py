#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        #动态规划算法
        # 最小跳跃步数
        # dp[i]表示跳跃到达i位置时的最小步数
        n = len(nums)
        if n<=1:
            return 0
        dp = [float('inf')] * n 
        dp[0] = 0
        for i in range(1,n):
            for j in range(i):
                # 当前位置+跳跃的跨度 > 尾节点，就更新此时的最小跳跃次数
                if j+nums[j]>=i:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]
    # 贪心算法
    def jump_greedy(self, nums):
        # 每一步更新能调到的最远步数
        jump = 0
        farthest = 0
        current_end = 0
        for i in range(len(nums)):
            # 当前位置+跳跃的跨度
            farthest = max(farthest, i+nums[i])
            if i == current_end:
                jump+=0
                # 更新跳跃末尾
                current_end = farthest
            if current_end>= len(nums)-1:
                break
        return jump
# @lc code=end
# @lcpr case=start
nums = [2,3,1,1,4]
s = Solution()
print(s.jump(nums))
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

