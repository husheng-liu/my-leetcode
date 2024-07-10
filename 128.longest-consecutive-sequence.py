#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30113
#
# [128] 最长连续序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
            return x

        # 路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # 按秩合并
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]

    def get_max_size(self):
        return max(self.size.values())

def longestConsecutive(nums):
    if not nums:
        return 0

    uf = UnionFind()

    for num in nums:
        uf.find(num)
        if num==2:
            print(uf.size)
            print(uf.parent) 
        uf.union(num, num + 1)
        if num==2:
            print(uf.size)
            print(uf.parent)
    return uf.get_max_size()

# 示例用法
nums = [100, 4, 200, 1, 3, 2]
result = longestConsecutive(nums)
print(result)  # 输出：4

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            
            if  num-1 not in nums:
                current_length = 1
                current_num = num
                while current_num+1 in nums:
                    current_length += 1
                    current_num += 1
                max_length = max(current_length, max_length)
        return max_length

# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

#

