#
# @lc app=leetcode.cn id=412 lang=python3
# @lcpr version=30118
#
# [412] Fizz Buzz
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n+1):
            if i %3 ==0 and i % 5 ==0:
                answer.append("FizzBuzz")
            elif i % 3 ==0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
# @lc code=end
s = Solution()
print(s.fizzBuzz(15))



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 15\n
# @lcpr case=end

#

