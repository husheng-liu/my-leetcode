#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30113
#
# [108] 将有序数组转换为二叉搜索树
#
class Solution:
    def sortedArrayToBST(self, nums):
        if nums is None:
            return
        mid = (0+len(nums))//2
        root = TreeNode(mid)
        # 一分为二进行左右拆分
        root.left = self.sortArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # if not nums:
        #     return None
        # mid = len(nums) //2
        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[:mid])
        # root.right = self.sortedArrayToBST(nums[mid+1:])

        # return root
        # 递归终止条件
        if not nums:
            return None
        mid = (0+len(nums))//2
        root = TreeNode(mid)
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

        
# @lc code=end



#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#

