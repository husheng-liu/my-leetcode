#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30117
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# 好的,让我用一个具体的二叉树例子来详细解释LCA算法:

# 假设有如下二叉树:

#        4 
#      /   \
#     2     6 
#    / \   / \ 
#   1   3 5   7

# 现在要找到结点1和结点5的最近公共祖先:

# 1. 从根节点4开始递归:

# - 查看4的左右子节点,分别递归左右子树找1和5
# - 左子树(2)找到1,返回2
# - 右子树(6)找到5,返回6

# 2. 由于左右子树都返回了节点,则结点4就是1和5的LCA

# 执行流程:

# - lowestCommonAncestor(4, 1, 5)
# - left = lowestCommonAncestor(2, 1, 5) => 找到1,返回2  
# - right = lowestCommonAncestor(6, 1, 5) => 找到5,返回6
# - left和right都不为null,则返回4

# 所以4就是1和5的最近公共祖先。

# 如果要找到1和3的LCA:

# - lowestCommonAncestor(4, 1, 3)
# - left = lowestCommonAncestor(2, 1, 3) => 找到1,返回2
# - right = lowestCommonAncestor(6, 1, 3) => 找不到，返回None
# - 只有left不为NULL,则返回left,即2就是1和3的LCA

# 通过递归地在子树中查找,就可以找到两个节点的第一个共同祖先节点。

# 这样理解过程是否清晰了些?有任何其他问题都可以问我。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # 没看明白这个
    # p, q 可能存在同一子树， 可能位于不同子树，p,q 之一为root
        if not root:
            return root
        # 节点和节点相等，不仅仅是val 相等。
        if root == p or root==q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)
        # p, q位于左右子树
        if left and right:
            return root
        # p, q 位于不同子树 
        return left if left else right

    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root==p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right 
# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#

