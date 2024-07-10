#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30113
#
# [105] 从前序与中序遍历序列构造二叉树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 递归终止条件
        if not preorder  and not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
# s = Solution()
# root = s.buildTree([3,9,20,15,7],[9,3,15,20,7])

# def preorderTraversal(root):
#     if not root:
#         return []
#     preorder = []
#     preorder.append(root.val)
#     preorder.extend(preorderTraversal(root.left))
#     preorder.extend(preorderTraversal(root.right))
#     return preorder

# print(preorderTraversal(root))
# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

