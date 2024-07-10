#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30113
#
# [118] 杨辉三角
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        dp = []
        # 
        for i in range(numRows):
            row = [1]*(i+1)
            # 注意这里的越界
            for j in range(1, i):
                row[j] = dp[i-1][j-1]+dp[i-1][j]
            dp.append(row) 
        return dp
s = Solution()
print(s.generate(2))
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

