#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30116
#
# [202] 快乐数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 不是快乐数的数称为不快乐数（英语：unhappy number），所有不快乐数的数字平方和计算，
# 最后都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中。
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # 用于存储已经出现过的数字
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))  # 计算每个位上数字的平方和
            if n in seen:
                print(n, seen)
                return False  # 如果出现循环序列但不包含1，返回False
            seen.add(n)  # 将当前数字加入到已经出现过的数字中
        return True  # 最终结果为1，返回True
s = Solution()
print(s.isHappy(37))
# @lc code=end


#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

