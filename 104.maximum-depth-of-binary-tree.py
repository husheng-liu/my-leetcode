#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30113
#
# [104] 二叉树的最大深度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 深度优先搜索是一种递归
        # 递归结束条件
        if root is None:
            return 0
        # 调用自身,缩减规模
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        result = max(leftDepth, rightDepth)+1
        return result
    
    def maxDepth(self, root):
        if root is None:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        result = max(leftDepth, rightDepth)+1
        return result
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

