#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30111
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        match = {")":"(", "}": "{", "]":"["}
        stack = []
        for char in s:
            if char in match:
                if not stack or stack[-1] != match[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return len(stack)==0
            
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

