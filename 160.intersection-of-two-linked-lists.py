#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30113
#
# [160] 相交链表
#

# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB
        # 两个交叉链表不等长，需要交叉指向对方的头节点，这样，循环最终会相交，
        # 而如果链表不相交，那么最终会同时指向None ,这样循环结束
        while currentA != currentB:
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        return currentA
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

