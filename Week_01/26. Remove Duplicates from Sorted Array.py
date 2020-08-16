# 快慢指针 时间复杂度O(n) 空间复杂度在传入的数组内操作并未新开空间O(1)
# 因为数组是有序的，那么重复的元素一定会相邻。删除重复元素，实际上就是将不重复的元素移到数组的左侧。当快指针的值等于慢指针的值时，j+1，当两者值不等时，说明快指针已经完成对重复元素的遍历，此时将快指针赋值给慢指针的后一个元素i+1，同时j继续移动j+1；最后需要返回无重复元素的数组长度，慢指针指向的元素即最后一个非重复元素，index比length小1，因此返回i+1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 特判 如果列表为空则直接返回
        if not nums:
            return 0
        # 慢指针i
        i = 0
        # 快指针j 
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:                
                nums[i+1] = nums[j]
                i += 1
        return i+1