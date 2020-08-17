# 回头看更多解法！
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        # 需要移动的元素个数为k除以nums长度的余数 例如[1,2,3,4] n=4 k=3时k%n=3，移动后为[2,3,4,1],如果k=5，k%n=1，那么移动一位就够了[4,1,2,3]，因为前四个移动等于没有移动；
        n = len(nums)
        k %= n
        # 先翻转整个数组，再翻转前k个实际被移动的元素，最后再翻转最后n-k个元素
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    # 定义一个helper func翻转数组，通过双指针指向头尾，头尾值交换，并且不断向中间缩窄直到双指针重叠或交叉完成；
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1

# 时间复杂度：O(n)， n 个元素被反转了总共 3 次。
# 空间复杂度：O(1)， 没有使用额外的空间。