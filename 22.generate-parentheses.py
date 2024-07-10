#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30111
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        backtrack("", 0, 0, n, result)
        return result
    
def backtrack(cur, open_count, close_count, n, result):
    # 递归终止条件
    if len(cur) == 2 * n:
        # print(cur)
        result.append(cur)
        print("result: ", result)
        return
    # 先递归 n 层， 再递归 n 层，之后从底层向上
        # 尝试添加左括号, 左括号加满了，就开始加右括号
    if open_count < n:
        print(cur)
        backtrack(cur + "(", open_count + 1, close_count, n, result)
        print("first finished")
    # 尝试添加右括号（前提是已使用的左括号数量大于右括号数量）
    if close_count < open_count:
        print("cur : ", cur)
        backtrack(cur + ")", open_count, close_count + 1, n, result)
        print("second finished")
    
solution = Solution()

solution.generateParenthesis(3)
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

