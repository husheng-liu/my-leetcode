#
# @lc app=leetcode.cn id=179 lang=python3
# @lcpr version=30116
#
# [179] 最大数
#
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    # def largestNumber(self, nums: List[int]) -> str:
        # # 冒泡排序+比较
        # def compare(a,b):
        #     a = str(a)
        #     b = str(b)
        #     if a+b>b+a:
        #         return -1
        #     else:
        #         return 1 
        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(n-1-i):
        #         if compare(nums[j],nums[j+1])==-1:
        #             nums[j], nums[j+1]= nums[j+1], nums[j]
        # nums = [str(item) for item in nums[::-1]]
        # return "".join(nums)
    def largestNumber(self, nums):
        # 归并排序
        def compare(a,b):
            a = str(a)
            b = str(b)
            if a+b>b+a:
                return -1
            else:
                return 1  
        def merge_sort(nums):

            if len(nums) <= 1:
                return nums
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)
        def merge(left, right):
            merge_ = []
            i, j = 0, 0
            while i< len(left) and j< len(right):
                if compare(left[i], right[j])==-1:
                    merge_.append(left[i])
                    i += 1
                else: 
                    merge_.append(right[j]) 
                    j += 1

            merge_.extend(left[i:])
            merge_.extend(right[j:])
            return merge_

        result = merge_sort(nums)
        if result[0] ==0:
            return "0"
        return ''.join(str(num) for num in result)
s = Solution()
print(s.largestNumber(nums = [0,0]))
# @lc code=end



#
# @lcpr case=start
# [10,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,30,34,5,9]\n
# @lcpr case=end

#

