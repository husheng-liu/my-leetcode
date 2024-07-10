#
# @lc app=leetcode.cn id=38 lang=python3
# @lcpr version=30111
#
# [38] 外观数列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        result = ''
        if n == 1:
            return '1'
        else:
            previous = self.countAndSay(n-1)
            
            count = 1
            for i in range(len(previous)):
                if i+1< len(previous) and previous[i]==previous[i+1]:
                    count += 1
                else:
                    # print("result: ", result)
                    result += (str(count)+previous[i])
                    count = 1
                    # print(result)
            return result
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1: return "1"

#         s  = self.countAndSay(n - 1) + "#"
#         ans, l = "", 0
#         for r in range(1, len(s)):
#             if s[r] != s[l]:
#                 ans += str(r - l) + s[l]
#                 l = r
#         return ans        


solution = Solution()
print(solution.countAndSay(3))
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

