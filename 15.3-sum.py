#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30111
#
# [15] 三数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums):
        # n = len(nums)
        # result = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1,n):
        #             if nums[i] + nums[j] + nums[k]==0:
        #                 if {nums[i], nums[j], nums[k]} not in result:
        #                     result.append([nums[i], nums[j], nums[k]])
        # result_ = [list(item) for item  in result]

        # return result_
        # 固定一个数，再用双指针
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            print(i)
            # i 跳过时不能向前看，因为如果向前看，
            # 相同下跳过会缩小选择空间，而应该向后看相同
            if  i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1 
            right = n-1
            while left< right:
                if nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left]== nums[left+1]:
                        left += 1
                    while left < right and nums[right]== nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#

