#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30118
#
# [287] 寻找重复数
#

# 输入：nums = [3,1,3,4,2]
# 输出：3
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # 因为数组元素有范围，【1，n】，数组中间值，比中间值大的元素个数
        # print(nums)
        start = 1
        end = len(nums)-1
        # while start< end:
        #     print(start, end)
        #     count = 0
        #     mid = (start + end)//2
        #     for num in nums:
        #         if num>=mid:
        #             count += 1
        #     if count>mid:
        #         start = mid + 1
        #     elif count<=mid:
        #         end = mid
        # 数组里面的元素[1,n]
        # start = 1
        # end = len(nums)-1
        # while start<= end:
        #     count_eq = 0
        #     count_big = 0
        #     count_small = 0
        #     mid = (start+end)//2
        #     for num in nums:
        #         if num==mid:
        #             count_eq +=1
        #         elif num>mid: 
        #             count_big += 1
        #         else:
        #             count_small += 1
        #     # print(count_eq)
        #     if count_eq> 1:
        #         return mid
        #     if count_big>end-mid:
        #         start = mid+1
        #     elif count_small>mid-start:
        #         end = mid-1
        while start< end:
            print(start, end)
            count = 0
            mid = (start + end)//2
            for num in nums:
                if num<= mid:
                    count += 1
            if count>mid:
                end = mid
            elif count<=mid:
                start = mid+1
        return start

# def func(nums, left, right):
#     count_eq, eq = 0,[]
#     count_big, big = 0,[]
#     count_small, small = 0,[]
#     mid = (left+right)//2
#     print(nums)
#     for num in nums:
        
#         if num==mid:
#             count_eq +=1
#             eq.append(num)
#         elif num>mid: 
#             count_big += 1
#             big.append(num)
#         else:
#             count_small += 1
#             small.append(num)
#         if count_eq> 1:
#             return mid
#         if count_big>mid:
#             left = mid+1
#             return func(big, left, right)
#         elif count_small>mid:
#             right = mid-1
#             return func(small,left, right)
# print(func([8,1,1,1,2,7,4,3,1,1], 1, 9))
s = Solution()
print(s.findDuplicate([8,9,9,9,9,7,4,3,9,9,1]))

# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#

