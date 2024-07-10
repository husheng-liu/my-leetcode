#
# @lc app=leetcode.cn id=324 lang=python3
# @lcpr version=30118
#
# [324] 摆动排序 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from random import seed, shuffle
import datetime



class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        mid = (0 + n-1) // 2 # 中位数索引
        

        # 快速排序中的一次划分
        def partition(begin,end):
            left,right = begin,end
            while left < right:
                while left < right and nums[left] < nums[right]:
                    right -= 1
                if left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
                while left < right and nums[left] < nums[right]: 
                    left += 1
                if left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    right -= 1
            return left
# [1,1,2,2,2,1]
        # 找到中位数对应的数值,确保nums[mid]左边小于，右边大于。
        left,right = 0, n-1
        while True:
            pivot = partition(left,right)
            # print(nums, pivot)
            if pivot == mid:
                break
            elif pivot > mid:
                right = pivot - 1
            else:
                left = pivot + 1
        
        # print(nums)
        # print(nums[mid])
        # 这个太有技巧性，面试不容易想到
        # target = nums[mid]
        # transAddress = lambda i: (2 * n - 2 * i - 1) % (n | 1)
        # k, i, j = 0, 0, n - 1
        # while k <= j:
        #     tk = transAddress(k)
        #     if nums[tk] > target:
        #         while j > k and nums[transAddress(j)] > target:
        #             j -= 1
        #         tj = transAddress(j)
        #         nums[tk], nums[tj] = nums[tj], nums[tk]
        #         j -= 1
        #     if nums[tk] < target:
        #         ti = transAddress(i)
        #         nums[tk], nums[ti] = nums[ti], nums[tk]
        #         i += 1
        #     k += 1
        # 三路划分(荷兰旗)
        midNum = nums[mid]
        left,curr,right = 0, 0, n-1
        while curr < right:
            if nums[curr] < midNum:
                nums[left],nums[curr] = nums[curr],nums[left]
                left += 1
                curr += 1
            elif nums[curr] > midNum:
                nums[curr],nums[right] = nums[right],nums[curr]
                right -= 1
            else:
                curr += 1
        print(nums)
        # 交叉合并
        small,big ,_nums = mid,n-1,nums[:]
        for i in range(n):
            if i%2 == 0:
                nums[i] = _nums[small]
                small -= 1
            else:#big
                nums[i] = _nums[big]
                big -= 1
    



s = Solution()
nums = [5,1,5,7,5,8,3,5]
s.wiggleSort(nums)
print(nums)
# @lc code=end



#
# @lcpr case=start
# [1,5,1,1,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,2,3,1]\n
# @lcpr case=end

#

