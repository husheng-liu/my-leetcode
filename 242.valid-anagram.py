#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30118
#
# [242] 有效的字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        for char in t:
            if char not in s_dict:
                return False
            else:
                s_dict[char] -= 1
        for k, v in s_dict.items():
            if v != 0:
                return False
            
        return True
s = Solution()
print(s.isAnagram(s = "anagram", t = "nagara"))
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#

