#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30113
#
# [148] 排序链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# 快慢指针，二分法，归并排序
from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         print("head: ", head.val)
#         if not head:
#             return None 
#         if not head.next:
#             return head
#         fast = head
#         slow = head 
#         prev = None
#         while fast and fast.next:
#             prev = slow
#             fast = fast.next.next
#             slow = slow.next
#             # print("___", slow.val) 
#             # if fast:
#             #     print(fast.val)
#             # else:
#             #     print("none")
#         # prev是slow 的浅拷贝，所以会改变slow,而此时，原来的slow 已经是slow.next
#         prev.next = None
#         left_head = head 
#         right_head = slow
#         # left 递归返回结果，right 递归再返回结果，
#         # 最后去merge. left,right的递归返回时会调用merge,进行归并排序 
#         # 递归到此直到遇到return,然后执行后续代码,后续代码执行完毕,此行代码才算结束,然后接着回到下一行代码
#         # 这种代码类似于进程执行到这里,循环转圈,然后循环完毕后,回到主干道,接着前进.
#         #       <___ 
#         #       |  | 
#         # ______|__|_____>
                            
#         left = self.sortList(left_head) 
#         print("left:", left.val)
#         right = self.sortList(right_head)
#         print("right:", right.val)

#         return self.merge(left, right)
#     # 4 -> 2 -> 1 -> 3 -> None
#     # 分割
#     # 4 -> 2 -> None
#     # 分割
#     # 4 -> None
#     # 2 -> None 
#     # 合并
#     # 2 -> 4 -> None
#     # 分割
#     # 1 -> 3 -> None
#     # 分割
#     # 1 -> None
#     # 3 -> None
#     # 合并
#     # 1 -> 3 -> None
#     # 最后合并

#     def merge(self, left:Optional[ListNode], right:Optional[ListNode]):
#         print(left.val, right.val)
#         dummy = ListNode(0) # 哑巴节点
#         current = dummy
#         while left and right:
#             if left.val < right.val:
#                 current.next = left
#                 left = left.next
#                 current = current.next
#             else: 
#                 current.next = right
#                 right = right.next
#                 current = current.next
#         if left:
#             current.next = left
#             # left = left.next
#             # current = current.next
#         if right:
#             current.next = right
#             # right = right.next
#             # current = current.next

#         return dummy.next


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def sortList(self, head):
        if head is None:
            return
        if head.next is None:
            return head 
        fast = head
        slow = head
        prev = None
       # 4 2 1 3
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        left_head = head
        right_head = slow
        left = self.sortList(left_head) 
        right = self.sortList(right_head)
        return self.merge(left, right)
        
    def merge(self,left, right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val<right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        # 此时左右两边的节点已经排好序了,所以不用while,用了while,就要cur 也要走.  
        while left:
            cur.next = left
            left = left.next
            cur = cur.next
        if right:
            cur.next = right
            right = right.next
            cur = cur.next
        return dummy.next

head = ListNode(5)
cur = head
for item in [7,6,8,3,1,2,4]:
   cur.next = ListNode(item) 
   cur = cur.next
cur.next = None

# while head:
#     print(head.val)
#     head = head.next
# head = ListNode(4)
# head.next = ListNode(2)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(3)
# head.next.next.next.next = None

s = Solution()
head = s.sortList(head)
while head:
    print(head.val)
    head = head.next


# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

