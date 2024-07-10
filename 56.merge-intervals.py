#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30113
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照区间的起始位置进行排序,保证其实位置从小到大排序，
        # 后面只需要排列末尾位置
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 前一个的尾部小于融合后的头部，则认为没有重叠
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
    
s = Solution()
print(s.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#

