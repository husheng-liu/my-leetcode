#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30118
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 哈希+排序
#         # nums_dict = {}
#         # for num in nums:
#         #     if num in nums_dict:
#         #         nums_dict[num] += 1
#         #     else:
#         #         nums_dict[num] = 1
#         # sorted_nums = sorted(nums_dict.items(), key=lambda x: x[1],reverse=True)
#         # result = []
#         # for item in sorted_nums:
#         #     result.append(item[0])
#         # return result[:k]
#         # 进行完频数统计，只需要对出现的频数找出前k大元素,找到kth largest频数，然后过滤即可。


#         def quick_select(nums,left, right, k):
#             if left == right:
#                 return nums[left]
#             povit_index = np.random.randint(left, right)
#             povit_index = partition(nums, left, right, povit_index)
#             if povit_index==k:
#                 return nums[k] 
#             if povit_index<k:
#                 return quick_select(nums, povit_index+1, right, k)
#             if povit_index>k:
#                 return quick_select(nums, left, povit_index-1, k)
#         def partition(nums, left, right, povit_index):
#             povit_freq = nums[povit_index]
#             nums[right], nums[povit_index] = nums[povit_index], nums[right]
#             store_index = left
#             for i in range(left, right):
#                 if nums[i]> povit_freq:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1
#             nums[right], nums[store_index] = nums[store_index], nums[right]
#             return store_index

        
#         nums_dict = {}
#         # nums_dict = {num:nums_dict.get(num, 0)+1   for num in nums}
#         for num in nums:
#             val = nums_dict.get(num, 0)+1
#             nums_dict[num]= val
#         freqs = list(nums_dict.values())
#         n = len(freqs)
#         top_k_freq = quick_select(freqs, 0, n-1, k-1)
#         result = []
#         for key,val in nums_dict.items():
#             if val>=top_k_freq:
#                 result.append(key)
#         return result 
import random

class Solution:
    def topKFrequent(self, nums, k):
        def quick_select(nums,k):
            povit = random.choice(nums)            
            small, equal, big = [],[],[]
            for num in nums:
                if num>povit:
                    big.append(num)
                elif num<povit:
                    small.append(num)
                else:
                    equal.append(num)

            if len(big)>=k:
                # 因为quick_select 是用来找nums里面第k大的元素，大于povit 的元素放在一起，
                # 原来第k大的依然第k大，不会改变其次序，因为比这个元素大的依然都在big里面
                # 如果是kth在small 里面的话就要重新计算它的次序，举个例子
                # [3,2,1,5,6,4]第3th大，如果选中5是povit,那么big =[6],samll=[3,2,1,4],equal=[5]
                # 那么4在small 里面，且排第一，只需要k减去比4大的元素个数，就是现在k在small 里面的排序。
                return quick_select(big, k)
            # 大于5，也就是大于等于6
            if len(small)>=len(nums)-k+1:
                return quick_select(small, k-len(big)-len(equal))
            # 不在big,不在small ,kth就在equal,equal里面都是一样的数字，直接返回。
            return povit
        dict_nums = {}       
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0)+1
        # print(dict_nums)
        freqs = list(dict_nums.values())
        
        top_kth_freq = quick_select(freqs,k)
        result = []
        for k, v in dict_nums.items():
            if v>=top_kth_freq:
                result.append(k)
        return result 
s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,2,3], k = 2)) 
# @lc code=end
#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

