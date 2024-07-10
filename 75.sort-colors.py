#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30113
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        blue = len(nums)-1
        red = 0
        cur = 0
        while cur <= blue:
            # 等于0 说明要和红区交换，交换后继续向前
            # 这里cur 要继续向前
            if nums[cur] == 0:
                nums[cur],nums[red] = nums[red],nums[cur]
                cur += 1
                red += 1
            # 先交换的都是最大或最小值，所以交换后都要挪动红区和蓝区
            elif nums[cur] == 2:
                nums[cur], nums[blue] = nums[blue],nums[cur]
                blue -= 1
            else:
                cur += 1
            print(nums)
        

    
s = Solution()
print(s.sortColors([2,0,2,1,1,0]))
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

