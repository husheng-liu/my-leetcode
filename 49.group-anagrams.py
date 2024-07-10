#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30111
#
# [49] 字母异位词分组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 采用key 是否存在代替str是否一样
        # 对于每一个str 都要比对这个str是否有字母异位词
        # 将字母异位词作为key,可以直接利用hash 是否存在该key
        # 来判断，实现转化，节省时间
        anagrams = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        
        return list(anagrams.values())
    
solution = Solution()
print(solution.groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))
# @lc code=end



#
# @lcpr case=start
# ["eat", "tea", "tan", "ate", "nat", "bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#

