#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30113
#
# [150] 逆波兰表达式求值
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        stack  = deque()
        for i in range(len(tokens)):
            if tokens[i] not in ['+','-','*','/' ]:
                stack.append(tokens[i])
            else:
                if len(stack) !=0:
                    right = stack.pop()
                    left = stack.pop()
                    res = self.func(tokens[i], left, right)
                    print(res)
                    stack.append(res)
        return stack.pop()

    def func(self,s, left, right):
        left = int(left)
        right = int(right)
        if s=='+':
            return left+right
        elif s== "-":
            return left - right
        elif s == "*":
            return left * right
        else:
            return int(left / right)
# s = Solution()
# print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# @lc code=end



#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#

