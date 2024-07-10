#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30113
#
# [155] 最小栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
#　只考虑一次get_min的情况
class MinStack:

    def __init__(self):
        self.minstack = []
        self.sorted_ele = []
    def push(self, val: int) -> None:
        self.minstack.append(val)
        print(self.sorted_ele)
        if len(self.sorted_ele)<1:
            self.sorted_ele.append(val)
        elif len(self.sorted_ele)==1:
            if self.sorted_ele[0]>val:
                self.sorted_ele.append(val)
            else:
                self.sorted_ele.insert(0,val)
        else:
            for i in range(len(self.sorted_ele)-1,0,-1):
                if val<=self.sorted_ele[len(self.sorted_ele)-1]:
                    self.sorted_ele.append(val)
                    break
                elif val>=self.sorted_ele[i] and val<=self.sorted_ele[i-1]:
                    self.sorted_ele.insert(i, val)
                    break
                else:
                    self.sorted_ele.insert(0,val) 
                    break


    def pop(self) -> None:
        return self.minstack.pop()

    def top(self) -> int:
        if len(self.sorted_ele)>0:
            return self.sorted_ele.pop(0)

    def getMin(self) -> int:
        return self.sorted_ele.pop()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(15)
# obj.push(18)
# obj.push(10)
# obj.push(7)
# obj.push(8)
# print(obj.sorted_ele)
# print(obj.pop())
# param_3 = obj.top()
# print(param_3)
# param_4 = obj.getMin()
# print(param_4)
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#

