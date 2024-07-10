#
# @lc app=leetcode.cn id=204 lang=python3
# @lcpr version=30116
#
# [204] 计数质数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 埃拉托斯特尼筛法
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2 :
            return 0
        primes = [1] * n
        primes[0]=primes[1]=0
# 2到根号n, 是因为再这里面需要判断每个i的2i，3i,4i....一直到30，
# 对于比根号n大的质数，已经再里面判断过了，所以不用重复判断。
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j]=0

        return sum(primes)
    
s = Solution()
print(s.countPrimes(30))


# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

