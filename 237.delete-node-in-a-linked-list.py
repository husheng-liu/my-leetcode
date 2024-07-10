#
# @lc app=leetcode.cn id=237 lang=python3
# @lcpr version=30117
#
# [237] 删除链表中的节点
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 4 5 1 9 ----> 4 1 9 
        # 按照要求不从内存中删除，那么给的那个node = ListNode(5), 可以将后一个的值和其相等，
        # 这时删除后一个即可，达到相同效果（node 前后循序相同）
        node.val = node.next.val
        # 指向，向前一步，要分清
        node.next = node.next.next
        
        
# @lc code=end



#
# @lcpr case=start
# [4,5,1,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,5,1,9]\n1\n
# @lcpr case=end

#

