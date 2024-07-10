#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30113
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    #     result = []
    #     current = []
    #     def is_palindrome(s):
    #         return s == s[::-1]
    #     def backtrace(start):
    #         if start == len(s):
    #             # print(current)
    #             #这里要创建副本，后续对current 的操作不会影响副本，
    #             # 但是直接append(current), 而不是副本，
    #             # 则后续对current的操作会对已经添加的结果产生影响。
    #             result.append(current[:])
    #             # print(result)
    #             return
    #         for i in range(start, len(s)):
    #             # 从开头截取i长度的字串，进行判断，
    #             # 如果已经属于回文串，则将其加入current,然后将接下来作为新的字符串进行递归。
    #             substr = s[start:i+1]
    #             if is_palindrome(substr):
    #                 current.append(substr)
    #                 backtrace(i+1)
    #                 current.pop()
    #     # 从0 开始回溯
    #     backtrace(0)
    #     return result


















    def partition(self, s:str):
        result = []
        n = len(s)
        current= [] 
        def is_parlindome(substr):
            if substr==substr[::-1]:
                return True

        def backtrack(start):
            if start == len(s):
                result.append(current[:])
                print(f"result：{result}")
                return
            for i in range(start, n):
                print(start, i)
                substr=s[start:i+1]
                print(f"substr: {substr}")
                if is_parlindome(substr):
                    current.append(substr)
                    backtrack(i+1)
                    current.pop()
        backtrack(0)
        return result
        
s = Solution()
# 使用列表作为示例
current = [1, 2, 3]

# 使用current
print(current)      # [1, 2, 3]
current[0] = 10
print(current)      # [10, 2, 3]

# 使用current[:]
new_current = current[:]
print(new_current)  # [10, 2, 3]
new_current[0] = 20
print(new_current)  # [20, 2, 3]
print(current)      #[10, 2, 3]
print(s.partition("aab"))
            
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

