#
# @lc app=leetcode.cn id=166 lang=python3
# @lcpr version=30116
#
# [166] 分数到小数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        sign = ''
        if numerator>0 and denominator<0 or numerator<0 and denominator>0:
            sign = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = numerator//denominator
        result = str(integer_part)
        if numerator%denominator==0:
            return sign+result
        
        result += '.'
        reminder = numerator%denominator
        reminder_map = {}
        while reminder:
            if reminder in reminder_map:
                index = reminder_map[reminder]
                result = result[:index]+"("+result[index:] + ")"
                break
            
            reminder_map[reminder] = len(result)
            reminder *= 10
            result += str(reminder//denominator)
            reminder %= denominator
        return sign+result
# @lc code=end



#
# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n333\n
# @lcpr case=end

#

