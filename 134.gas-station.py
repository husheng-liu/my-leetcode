#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30113
#
# [134] 加油站
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 这个问题是经典的加油站环路问题，可以使用贪心算法来解决。贪心算法的思路是，从任意一个加油站出发，
# 尽可能多地走到下一个加油站，直到无法继续走下去。然后再从下一个加油站开始重新尝试。
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start = 0
        # #每一步的剩余总油量
        # total_gas = 0
        # #当前可以获得的油量
        # # curr_gas = 0
        # for i in range(len(gas)):
        #     # curr_gas = curr_gas+gas[i]
        #     # 在任何两个加油站之间的total_gas < 0 则需要重新选择起点
        #     # 从total_gas=0开始，先加油，再耗油
        #     total_gas = total_gas + gas[i]-cost[i]
   
        #     print(total_gas)
        #     if total_gas<0:
        #         start += 1
        #         total_gas =  0
       
        # if total_gas>=0:
        #     return start 
        # else:
        #     return -1
        n = len(gas)
        total_gas = 0  # 总剩余汽油量
        cur_gas = 0  # 当前加油站剩余的汽油量
        start = 0  # 出发加油站的编号

        for i in range(n):
            # total_gas 积累每次尝试之后的剩余油量，其实就是总加油量-总耗油量
            total_gas += gas[i] - cost[i]
            # cur_gas 当前加油站的剩余油量
            cur_gas += gas[i] - cost[i]

            # 如果当前汽油不够到达下一个加油站，将起始站点设为下一个加油站
            if cur_gas < 0:
                start = i + 1
                cur_gas = 0

        # 如果总剩余汽油量小于0，说明无法环绕一圈
        if total_gas < 0:
            return -1
        else:
            return start
        
s = Solution()
print(s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#

