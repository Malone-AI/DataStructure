#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        balanced=True
        index=0
        while index<len(s) and balanced:
            symbol=s[index]
            if symbol in '({[':
                stack.append(symbol)
            else:
                if stack==[]:
                    balanced=False
                else:
                    top=stack.pop()
                    if not self.match(top,symbol):
                        balanced=False
            index=index+1
        if stack==[] and balanced:
            return True
        else:
            return False

    def match(self,open,close):
        opens='({['
        closers=')}]'
        return opens.index(open)==closers.index(close)
# @lc code=end,
