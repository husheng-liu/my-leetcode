#
# @lc app=leetcode.cn id=454 lang=python3
# @lcpr version=30118
#
# [454] 四数相加 II
#
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # n = len(nums1)
        # count = 0
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             for l in range(n):
        #                 if nums1[i] + nums2[j]+nums3[k]+nums4[l] == 0:
        #                     count += 1
        # return count
        counter12 = Counter([i+j for i in nums1 for j in nums2])
        count = 0
        for k in nums3:
            for l in nums4:
                if -k-l in counter12:
                    count += counter12[-k-l]
        return count

s = Solution()
print(s.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
# @lc code=end



#
# @lcpr case=start
# [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n[0]\n[0]\n
# @lcpr case=end

#

