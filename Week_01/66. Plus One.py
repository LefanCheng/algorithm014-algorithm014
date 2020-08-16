# 第一遍，参考高票答案，递归解法
# 1,2,3 -> 1,2,4
# 1,3,9 -> 1,4,0
# 1,9,9 -> 2,0,0
# 3,8,9,9,9 -> 3,9,0,0,0
# 1,9,8,9 -> 1,9,9,0
# 9,9 -> 1,0,0

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if digits has only one element and it's 9, assuming no empty list. In the recursion below, if the first digit is 9, such as [9, 9, 9], the list passed in the recursion will be [9], this base case will return [1, 0], so that final result would be [1, 0, 0, 0]
        if len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        
        # if the last digit doesn't equal to 9, plus one and return
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
            
        # if the last digit equals to 9, turn it to 0. then repeate the same process to the rest of list digits[:-1]
        if digits[-1] == 9:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            
        return digits
    
#tc: n times recursion X O(1) each recursion = O(n)
#sc: O(n^2)? each time digits[:-1] will be copied and passed in the function itself in the recursion.