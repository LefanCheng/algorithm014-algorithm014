# 超哥：考虑可能的解法，再比较不同解法
# 1. 两个指针，一个记录0的位置，Loop统计0个数，将非零元素往前挪，零元素往后放，两个循环
# 2. 新开数组，碰到0往新数组后面放，非0往前放，两个指针i指向头，j指向尾。但不符合本题要求，同时空间复杂度更高；
# 3. 直接在内存中进行Index操作，遍历一维数组，开一个j记录非零元素位置，如果nums[i]等于0就不用处理， 如果nums[i]不等于0的话，就要把nums[i]放到nums[j]这个位置，因为j始终记录下一个非0元素要放得位置。如果i不等于j的话，nums[i]的位置赋值为0。之后j++;
# 解法1.1
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 两个指针i和j
				# 指针j记录下一个非零元素放置的位置
        j = 0
        for i in range(len(nums)):
						if nums[i] != 0:
								
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                j += 1
        return nums
# 解法1.2 利用python交换元素方便特性
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
				# 当前元素!=0，就把其交换到左边，等于0的交换到右边（所有的0都是0？）
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
# 时间复杂度:O(n)
# 代码执行的总操作（数组写入）是非 0 元素的数量。这比解决方案2的复杂性（当大多数元素为 0 时）要好得多。但是，两种算法的最坏情况（当所有元素都为非 0 时）复杂性是相同的。
# 空间复杂度:O(1)

# 解法2 两遍遍历
# 创建两个指针i和j，第一次遍历的时候指针j用来记录当前有多少非0元素。即遍历的时候每遇到一个非0元素就将其往数组左边挪，第一次遍历完后，j指针的下标就指向了最后一个非0元素下标。第二次遍历的时候，起始位置就从j开始到结束，将剩下的这段区域内的元素全部置为0。

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
				# 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        # 非0元素统计完了，剩下的都是0了
				# 所以第二次遍历把末尾的元素都赋为0即可
        for i in range(j, len(nums)):
            nums[i] = 0

        return nums
# 时间复杂度:O(n)
# 空间复杂度:O(1)print('hello world')