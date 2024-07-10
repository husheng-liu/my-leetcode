#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30113
#
# [102] 二叉树的层序遍历
# 从上到下 从左到右


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import Optional, List
from collections import deque

# 广度优先搜索
class Queue:
    def __init__(self) -> None:
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def is_empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def __len__(self):
        return len(self.queue)


# Definition for a binary tree node.
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 采用队列保存每一个层的节点
        # queue = Queue()
        # if root is None:
        #     return []
        # queue.enqueue(root)
        # result = [] 
        # while not queue.is_empty():
        #     level_size = len(queue)
        #     current_level = []
        #     for _ in range(level_size):     
        #         node = queue.dequeue()
        #         current_level.append(node.val)
        #         if node.left:
        #             queue.enqueue(node.left)
        #         if node.right:
        #             queue.enqueue(node.right)
        #     result.append(current_level) 
        # return result
        # 双端队列deque
        queue = deque()
        result = []
        queue.append(root)
        while len(queue)>0:
            current_level = []
            level_size = len(queue)
            # 不要直接用len(deque)
            # 只把这一层里面的几点节点弹出
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level.append(node.val)
            result.append(current_level) 
        return result
    
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s = Solution()
print(s.levelOrder(root))

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

