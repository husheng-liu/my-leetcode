#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30113
#
# [98] 验证二叉搜索树
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSThelper(node, lower, upper):
            if node is None:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            # 左子树的上界是节点的值，右子树的下界是节点的值
            return isValidBSThelper(node.left, lower, node.val) and isValidBSThelper(node.right, node.val, upper)
        return isValidBSThelper(root, float('-inf'), float('inf'))


#     def isValidBST(self, root):
#         def inorderTraversal(node):
           
#             if node is None:
#                 return []
#             print(node.val)
#             # return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)
#             return inorderTraversal(node.right) + inorderTraversal(node.left) 
        
#         inorder = inorderTraversal(root)
#         print(inorder)
#         for i in range(1, len(inorder)):
#             if inorder[i] <= inorder[i-1]:
#                 return False
#         return True
    
# # 创建二叉搜索树
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
# s = Solution()
# print(s.isValidBST(root))

# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#

