#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30111
#
# [2] 两数相加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:

#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         cur = dummy = ListNode()  # 哨兵节点
#         carry = 0  # 进位
#         while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
#             carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 节点值和进位加在一起
#             cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
#             carry //= 10  # 新的进位
#             cur = cur.next  # 下一个节点
#             if l1: l1 = l1.next  # 下一个节点
#             if l2: l2 = l2.next  # 下一个节点
#         return dummy.next  # 哨兵节点的下一个节点就是头节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self,l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            summation = x + y + carry
            carry = summation // 10
            curr.next = ListNode(summation % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            curr.next = ListNode(1)

        return dummy.next
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/add-two-numbers/solutions/2327008/dong-hua-jian-ji-xie-fa-cong-di-gui-dao-oe0di/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

