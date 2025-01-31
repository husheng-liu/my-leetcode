#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30111
#
# [36] 有效的数独
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # 验证行
                    if num in rows[i]:
                        return False
                    rows[i].add(num)

                    # 验证列
                    if num in cols[j]:
                        return False
                    cols[j].add(num)

                    # 验证3x3宫
                    # 让按行落下的数字分配到不同的宫内（即boxes里面的set)，例如
                    # 第一行落到 0，0，0，1，1，1，2，2，2
                    #           0，0，0，1，1，1，2，2，2
                    #           0，0，0，1，1，1，2，2，2
                    #           3，3，3，4，4，4，5，5，5 
                    #           3，3，3，4，4，4，5，5，5 
                    #           3，3，3，4，4，4，5，5，5 
                    #           6，6，6，7，7，7，8，8，8
                    #           6，6，6，7，7，7，8，8，8
                    #           6，6，6，7，7，7，8，8，8
                                
                    box_index = (i // 3) * 3 + j // 3
                    if num in boxes[box_index]:
                        return False
                    boxes[box_index].add(num)

        return True
# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

