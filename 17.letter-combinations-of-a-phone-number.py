#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30111
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 采用递归的方式处理，取代多层循环
        if len(digits) == 0:
            return []
        output = []
        phone = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"}
        def backtrack(combination, next_digits, output):
            if len(next_digits) == 0:
                print(combination)
                output.append(combination)
            else:
                for letter in phone[next_digits[0]]: 
                    # 循环的
                    backtrack(combination+letter, next_digits[1:],output)
        backtrack("", digits, output)
        return output
# 假设digits 为n个，该题并不是n的次方的算法复杂度，而是要考虑digits
# 中对应的letter的数量。
solution = Solution()
print(solution.letterCombinations("23"))
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

