#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30113
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # capacity：缓存的容量
        # cache：一个哈希表，用于存储键值对的信息，键是缓存中的键，
        # 值是指向双向链表节点的指针
        # head：指向双向链表的头节点，表示最近使用的节点
        # tail：指向双向链表的尾节点，表示最久未使用的节点
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove.node
            self._add.node
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove.node
            node.val = value
            self._add.node
        else:
            if len(self.cache)>= self.capacity:
                del self.cache[self.tail.prev.key]
                # 从链表中删除最久未使用的
                # 当我们需要删除尾节点时，也就是最久未使用的节点时，直接删除尾节点是可以实现LRU缓存的淘汰策略的。
                # 然而，在实际的实现中，我们通常使用哑节点（dummy node）作为头节点和尾节点，而不是直接使用存储键值对的节点。哑节点是一个不存储实际数据的虚拟节点，它的存在可以简化链表操作，并且可以避免在特殊情况下需要处理头节点或尾节点的特殊逻辑。
                # 在LRUCache类的实现中，我们使用了哑节点作为头节点和尾节点。这样，无论是插入新节点还是删除节点，都可以使用相同的逻辑，而不需要额外的特殊处理。当需要删除最久未使用的节点时，我们删除尾节点的前一个节点，而不是直接删除尾节点本身，是因为这样可以避免处理特殊情况下的逻辑，同时保持代码的简洁性和一致性。
                # 总结起来，使用哑节点作为头节点和尾节点可以简化链表操作，并且避免特殊情况下的处理逻辑。因此，在LRUCache类的实现中，我们选择删除尾节点的前一个节点，而不是直接删除尾节点。
                self._remove(self.tail.prev)
            node = ListNode(key, value)
            self.cache[key] = value
            self._add(node)


    def _add(self, node):
        # 将节点插到头节点之后
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node 
        pass

    def _remove(self, node):
        # 从链表中移除节点
        prev = node.prev
        next = node.next
        node.prev.next = node.next
        node.next.prev = node.prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



