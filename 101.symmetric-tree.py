#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30113
#
# [101] 对称二叉树
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #　这个递归的过程还是有点没搞清楚。
        # def isSymmetricHelper(left, right):
        #     if left is None and right is None:
        #         return True
        #     if  left is None or right is None or left.val != right.val :
        #         return False
        #     return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
        # if root is None:
        #     return True
        # return isSymmetricHelper(root.left, root.right)
    
    # def isSymmetric(self, root)->bool:
        # 这里的left,right 是对称的两个节点，不是一个节点的两个节点
        def isSymmetricHelper(left, right):
            if left is None and right is None:
                return True
            if left.val != right.val or left is None or right is None:
                return False
            return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(left.right, right.left)
        if root is None:
            return True

        return isSymmetricHelper(root.left, root.right)
# root = [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmetric(root)) 

# @lc code=end


#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

