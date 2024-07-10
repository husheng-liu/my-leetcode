#
# @lc app=leetcode.cn id=210 lang=python3
# @lcpr version=30116
#
# [210] 课程表 II
#

# @lc code=start
# 要的是拓扑排序的顺序
from typing import List
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        queue = deque()
        # 计算入度
        result = []
        for prerequisite in prerequisites:
            indegree[prerequisite[0]] += 1
        # print(indegree)
        # 入读为0的放入队列
        for i  in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        # print(queue)
        while queue:
            course = queue.popleft()
            numCourses -= 1
            result.append(course)
            for prerequisite in prerequisites:
                if prerequisite[1] == course:
                    indegree[prerequisite[0]] -= 1
                    if indegree[prerequisite[0]]== 0:
                        queue.append(prerequisite[0])
        if numCourses==0:
            return result
        else:
            return []
s = Solution()
print(s.findOrder(numCourses=3, prerequisites=[[1,0],[1,2],[0,1]]))  

                
            

# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0],[2,0],[3,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

#

