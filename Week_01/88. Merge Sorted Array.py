# 方法一 : 合并后排序
# 最朴素的解法就是将两个数组合并之后再排序。
# 时间复杂度 : O((n + m)log(n + m))（为什么？）
# 空间复杂度 : O(1)。
# 该方法时间复杂度高因没有利用两个数组本身已经有序这一点。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2)
# 方法二 : 双指针 / 从前往后
# 一般而言，对于有序数组可以通过 双指针法 达到O(n + m)的时间复杂度。最直接的算法实现是将指针p1 置为 nums1的开头， p2为 nums2的开头，在每一步将最小值放入输出数组中。由于 nums1 是用于输出的数组，需要将nums1中的前m个元素放在其他地方，也就需要 O(m)的空间复杂度。
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Make a copy of nums1.
        nums1_copy = nums1[:m] 
        nums1[:] = []

        # Two get pointers for nums1_copy and nums2.
        p1 = 0 
        p2 = 0
        
        # Compare elements from nums1_copy and nums2
        # and add the smallest one into nums1.
        while p1 < m and p2 < n: 
            if nums1_copy[p1] < nums2[p2]: 
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # if there are still elements to add
        if p1 < m: 
            nums1[p1 + p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]

# 方法三 : 双指针 / 从后往前 最优解
# 方法二已经取得了最优的时间复杂度O(n + m)O(n+m)，但需要使用额外空间。这是由于在从头改变nums1的值时，需要把nums1中的元素存放在其他位置。
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
				# m-1，n-1为双指针，命名为p1, p2，分别指向nums1(nums[:m])与nums2的尾部(nums1[m-1]之后的元素为placeholder值为0)，同时通过 m+n-1 第三个指针p3指向nums1数组的尾部，因为输出的是nums1本身，我们需要直接修改内部元素
				#	当 p1 >= p2 时 p3 = p1, p1向左移动一位，否则 p3 = p2, p2向左移动一位，当m和n有一方为0时，p1、p2无法再进行比较，循环结束。
				# 额外的基本情况：当p1或p2有一个率先结束，loop停止，例如num1 = [0], m=0, nums2 = [1], n=1, p1、p2无法比较，loop不会启动，此时nums2中剩下元素一定小于p3之后的元素，因此只需要把nums2里面全部元素放入nums1中即可，如果是p2先结束，p1剩下的元素一定小于nums2里面所有元素，因此什么都不用做；
				# 当 m 大于 0 且 n 也大于 0 时
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

# 时间复杂度 : O(n + m)O(n+m)。
# 空间复杂度 : O(1)O(1)。print('hello world')