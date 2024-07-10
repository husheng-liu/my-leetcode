#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30113
#
# [116] 填充每个节点的下一个右侧节点指针
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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
    

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = Queue()
        queue.enqueue(root)

        while not queue.is_empty():
            prev_node = None
            level_size = len(queue)

            for _ in range(level_size):
                cur_node = queue.dequeue()
                # 当每一层的当前节点的前一个节点存在的时候，将当前节点作为前一个节点的next
                # 反之，对于完美二叉树，当前节点肯定实在最左侧，将其跳过，就会满足上面的条件。
                # 因为node.val 默认都是None, 所以右侧边缘的节点不用改，只需要改动除右侧边缘的节点
                if prev_node:
                    prev_node.next = cur_node
                prev_node = cur_node
                if cur_node.left:
                    queue.enqueue(cur_node.left)
                if cur_node.right:
                    queue.enqueue(cur_node.right)

        return root
    
    def connect(self,root:'Optional[Node]')->'Optional[Node]':
        queue = deque()
        queue.append(root)
        while len(queue)>0:
            prev_node = None
            level_size = len(queue)
            for _ in range(level_size):
                cur_node = queue.popleft()
                if prev_node:
                    prev_node.next = cur_node
                # 无论是不是prev_node=None 都要执行这一步
                prev_node = cur_node
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
        return root

        

root = Node(1)
root.left = Node(2)        
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s = Solution()
root = s.connect(root)
print(root.left.next.val)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

