#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30116
#
# [207] 课程表
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
# 3 0 1 1 2 2 1
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        queue = deque()
        for course in prerequisites:
            # course[0]（课程0）出现几次就表示入度为几
            indegree[course[0]]  += 1
        # 所有入度为0的放入队列
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        # 所有入度为零的课程的先修课程,先上先修课程，上完这些课程就可以上以这些课程为基础的课程，成为高阶课程。
        # 先修课程完成，高阶课程正好入度为0，则作为先修课程，重复下去，直到全部课程上完。
        # 
        while queue:
            course = queue.popleft()
            numCourses -= 1
            for prerequisite in prerequisites:
                if prerequisite[1] == course:
                    indegree[prerequisite[0]]-= 1
                    if indegree[prerequisite[0]] == 0:
                        queue.append(prerequisite[0])
        return numCourses == 0

s = Solution()
print(s.canFinish(numCourses=2, prerequisites=[[1,0]]))                    

        
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#

