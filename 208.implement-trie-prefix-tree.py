#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30116
#
# [208] 实现 Trie (前缀树)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # 从左到右会将相同的放在一起，不同的地方分开
        # children不是一个节点，而是一个可以存放多个节点的字典，
        # 这样保存分开的字符，这些字符是key,对一个的value是一个TrieNode
        node  = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end



