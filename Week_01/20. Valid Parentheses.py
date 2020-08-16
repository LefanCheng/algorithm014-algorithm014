# 剥洋葱
# 解法1：暴力 不断replace匹配的括号对为"" 直到整个string变成空string O(n^2) 双层遍历 每次
# (({[]})) -> (({})) -> (()) -> () -> ""
# 解法2：Stack O(n) 遍历一遍 空间复杂度O(n)
# ([]{}) 合法的洋葱最内部一定是一对紧挨着的括号，所以stack后进先出，从左到右遍历，如果遇到合法的最内部紧挨括号，这对括号就会两两抵消；
class Solution:
    def isValid(self, s: str) -> bool:
        # 如果传入的String的character字符个数为奇数，直接返回False省去多余计算
        if len(s) % 2 == 1:
            return False
        # 遇到左括号把对应的右括号压入栈，当遇到右括号检查栈是否为空，为空则一定没有对应左括号可以匹配，返回False，如果栈不为空，把栈顶元素也就是前面压入的左括号对应的右括号弹出，检查是否与当前右括号匹配，如果不匹配则返回False。最后检查栈是否为空，为空说明压入的对应的右括号全部遇到匹配的右括号抵消了。
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif not stack or stack.pop() != c:
                return False
        
        return not stackprint('hello world')