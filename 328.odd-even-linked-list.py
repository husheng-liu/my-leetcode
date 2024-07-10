#
# @lc app=leetcode.cn id=328 lang=python3
# @lcpr version=30118
#
# [328] 奇偶链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
# 1 2 3 4 5 6 7 8 
# 1 -> 3 2->4 3->5 4->6
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        odd_head = head
        even_head = head.next
        odd = odd_head
        even = even_head
        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return odd_head
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,5,6,4,7]\n
# @lcpr case=end

#

