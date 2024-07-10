#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30111
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    # 双指针，每次移动最长值都会变动一次。
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        longest = 0
        sub_string=[]
        while left<len(s) and right < len(s):
            if s[right] not in sub_string:
                sub_string.append(s[right])
                right += 1
                longest = max(longest, right- left)
            else:
                sub_string.remove(s[left])
                left += 1
        return longest
                 
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

