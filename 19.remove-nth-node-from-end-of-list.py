#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30111
#
# [19] 删除链表的倒数第 N 个结点
#

from typing import List ,Optional
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.

# 这个问题的核心是怎样显示出倒数第n个指针。解决方法是采用快慢指针的方式。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        # 这里让slow 保持slow.next就在应该拆掉的那个node 上。
        while fast.next is not None:
            # fast.next 赋值给fast 表示fast 向前走了一步。
            fast = fast.next
            slow = slow.next
        # 尾节点可以指向空节点
        slow.next = slow.next.next 
        return dummy.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

