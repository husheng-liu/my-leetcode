#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30113
#
# [94] 二叉树的中序遍历
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from typing import  Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderHelper(root, result)
        return result
    def inorderHelper(self,node, result):
        if node:
            self.inorderHelper(node.left, result)
            result.append(node.val)
            self.inorderHelper(node.right, result)
        
class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while curr or stack:

            # 先遍历左子树，塞进栈内
            while curr:
                stack.append(curr)
                curr = curr.left
            # 然后放出，先放出的为后进去的，也就是最左侧的节点
            curr = stack.pop()
            # 放出后进入结果列表
            result.append(curr.val)
            # 然后处理右子树
            curr = curr.right
        return result
# 创建节点
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.inorderTraversal(root))
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

