#
# @lc app=leetcode.cn id=217 lang=python3
# @lcpr version=30116
#
# [217] 存在重复元素
#
# 输入：nums = [1,1,1,3,3,4,3,2,4,2]
# 输出：true

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # dup = []
        # for num in nums:
        #     # 列表的查找（in)操作是O(n)
        #     if num in dup:
        #         return True
        #     dup.append(num)
        # return False
        # return len(nums)!=len(set(nums))
        seen = set()
        for num in nums:
            # 哈希的查找操作时O(n)
            if num in seen:
                return True
            seen.add(num)
        return False
            
s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,3,3,4,3,2,4,2]\n
# @lcpr case=end

#

