#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30102
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 和二分查找有本质区别
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """以下为错误解法，原因：1 错误认为有序，从而直接可以固定一个，二分查找另一个
        单纯的二分查找是不需要满足条某个条件的，而这个需要满足一个条件,其实这样也可以写"""
        # j = len(nums)//2
        # for i in range(len(nums)):
        #     while i< j< len(nums):
        #         if nums[j] > target-nums[i]:
        #             j = j//2
        #         elif nums[j] < target-nums[i]:
        #             j = (len(nums)-j)//2
        #         else:
        #             return [i,j] 
        # 这种解法相当于固定一个，查找另一个满足的，查找另一个的算法可能是二分，也可能遍历,
        # 但是面试还是需要自己写
        def binary_search(self, arr:list, a:int):
            # 这个arr并不是有序的,需要先排序
            arr = sorted(arr)
            left, right = 0, len(arr)-1
            middle = (left+right)//2
            while left< right:
                if arr[middle]== a:
                    return True
                else: 
                    return False

                
        n = len(nums)
        for i in range(n):
            if target-nums[i] in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
        return []
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

