#
# @lc app=leetcode.cn id=95 lang=python3
# @lcpr version=30204
#
# [95] 不同的二叉搜索树 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# from typing import List, Optional
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # if n == 0:
        #     return [] 
        # def buildTrees(start, end):
        #     if start>end:
        #         return [None]
        #     trees = []
        #     for k in range(start, end+1):
        #         left_trees = buildTrees(start, k-1)
        #         right_trees = buildTrees(k+1, end)
        #         for l in left_trees:
        #             for r in right_trees:
        #                 root = TreeNode(k)
        #                 root.left = l
        #                 root.right = r
        #                 trees.append(root)
        #     return trees
        
        # return buildTrees(1, n)
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if(n==0):
            return []
        def build_Trees(left,right):
            all_trees=[]
            if(left>right):
                return [None]
            for i in range(left,right+1):
                left_trees=build_Trees(left,i-1)
                right_trees=build_Trees(i+1,right)
                for l in left_trees:
                    for r in right_trees:
                        cur_tree=TreeNode(i)
                        cur_tree.left=l
                        cur_tree.right=r
                        all_trees.append(cur_tree)
            return all_trees
        res=build_Trees(1,n)
        return res
        
# @lc code=end
s = Solution()
print(s.generateTrees(3))


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

