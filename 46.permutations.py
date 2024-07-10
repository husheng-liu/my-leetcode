#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30111
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import copy


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums)==1:
    #         return [nums]
    #     if len(nums) ==2:
    #         return [nums, nums[::-1]]

    #     if len(nums)>2:
    #         result = []
    #         print("permute: ", self.permute(nums[:-1]))
    #         for item in self.permute(nums[:-1]):
    #             print(f"item: {item}")
                
    #             for i in range(len(item)+1):
    #                 item.insert(i, nums[-1])
    #                 print(f"item inserted: {item}")
    #                 #这里不直接append item ，因为item后面会进行
    #                 # pop 处理，进行处理之后，也会影响前面 append 的结果。
    #                 #　所以再后面处理之前，将现有的结果进行深度拷贝，这样
    #                 # 就会新开内存进行一个新的变量，而不是保存一个指针（refer)
    #                 item_ = copy.deepcopy(item)
    #                 # 等号是一种浅拷贝
    #                 # item_ = item
    #                 result.append(item_)
    #                 print(f"result: {result}")
    #                 item.pop(i)
    #                 # item = item_
    #                 print(f"item1: {item}")
    #         return result

    def permute(self, nums):
        def backtrack(start):
            # 当到达数组末尾时，将当前排列添加到结果列表
            if start == len(nums):
                result.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    # 交换当前位置与后面位置的元素
                    nums[start], nums[i] = nums[i], nums[start]
                    # 继续递归生成下一位的排列
                    backtrack(start + 1)
                    # 恢复数组，以便进行下一次交换
                    nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
solution = Solution()
print(solution.permute([1,2,3,4]))
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

