#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30113
#
# [103] 二叉树的锯齿形层序遍历
#

from collections import deque
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List, Optional

# Definition for a binary tree node.
class Queue:
    def __init__(self):
        self.queue = []
    def __len__(self):
        return len(self.queue)
    def __iter__(self):
        for item in self.queue:
            yield item 

    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def enqueue_left(self, item):
        return self.queue.insert(0, item)
    def is_empty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     queue = Queue()
    #     queue.enqueue(root)
    #     result = []
    #     is_left_to_right = True
    #     if root is None:
    #         return []
        
    #     while not queue.is_empty():
    #         level_size = len(queue)
    #         current_level = Queue()
    #         for _ in range(level_size):
    #             node = queue.dequeue()

    #             if is_left_to_right:
    #                 current_level.enqueue(node.val)
    #             else:
    #                 current_level.enqueue_left(node.val)
    #             if node.left:
    #                 queue.enqueue(node.left)
    #             if node.right:
    #                 queue.enqueue(node.right)
    #         result.append(list(current_level))
    #         is_left_to_right = not is_left_to_right

    #     return result
    # 采用奇偶来控制也行，但是节点是从队列中依次弹出，不能够实现从后先前弹出
    # 所以保持节点的依次弹出，而采用双端队列将数据从后先前插入
    from collections import deque
    def zigzagLevelOrder(self, root):
        queue = deque()
        queue.append(root)
        is_left_to_right = True
        result = []
        while len(queue)>0:
            current_level = deque()
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if is_left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(list(current_level))
            # 一层结束,变换方向
            is_left_to_right = not is_left_to_right 
        return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

s = Solution()
print(s.zigzagLevelOrder(root))
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

