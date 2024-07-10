#
# @lc app=leetcode.cn id=350 lang=python3
# @lcpr version=30118
#
# [350] 两个数组的交集 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 不在排序的情况下，哈希
        # o(N)
        # counter = Counter(nums1)
        # result = []
        # for num in nums2:
        #     if num in counter:
        #         if counter[num]>0:
        #             result.append(num)
        #         # 要么你先遍历完，要么我先减完
        #             counter[num]-=1
        # return result
        # 排序的情况下
        nums1.sort()
        nums2.sort()
        left1 = 0
        left2 = 0
        result = []
        while left1<len(nums1) and left2<len(nums2):
            print(left1, left2)
            print(nums1[left1], nums2[left2])
            if nums1[left1]==nums2[left2]:
                result.append(nums1[left1])
                left1+=1
                left2+=1
            elif nums1[left1]<nums2[left2]:
                left1+=1
            else:
                left2+=1
        return result
s = Solution()
print(s.intersect([1,2,2,1],[2,2]))
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

