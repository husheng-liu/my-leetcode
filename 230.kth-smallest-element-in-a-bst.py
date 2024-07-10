#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30116
#
# [230] 二叉搜索树中第K小的元素
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
from typing import Optional

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 快速选择
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # 记录当前遍历到的节点个数
        self.result = None  # 存储第K小的元素
        
        def inorderTraversal(node: TreeNode):
            if node is None:
                return
          
            inorderTraversal(node.left)  # 递归遍历左子树
            
            self.count += 1  # 计数器加1
            
            if self.count == k:  # 当计数器等于K时，找到第K小的元素
                self.result = node.val
                return
            
            inorderTraversal(node.right)  # 递归遍历右子树
        
        inorderTraversal(root)  # 调用中序遍历函数
        return self.result

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # 当将 count 和 result 定义为整数和 None 值时，由于整数和 None 是不可变类型，无法在递归过程中直接修改它们的值。
    # 在 Python 中，函数参数是按值传递的，意味着在函数内部对参数的修改不会影响到外部的变量。
#         count = 0
#         result = None
#         def inorderTraversalhelper(node,count, result):
#             if node is None:
#                 return
#             inorderTraversalhelper(node.left, count, result)
#             count += 1
#             if k == count:
#                 result =  node.val
#                 return 
#             # result.append(node)
#             # if len(result) == k:
#                 # return node.val
#             inorderTraversalhelper(node.right, count, result)
#             # if len(result) == k:
#                 # return node.right.val
#         inorderTraversalhelper(root, count, result)
#         return result

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
s = Solution()
print(s.kthSmallest(root, 5))
                

# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#

