# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Base Case 终止条件
        # 当上一个递归传入的l2.next也就是当前新的l2为None时，None和l1的值无须比大小，直接返回l1的值
        if not l2:
            return l1
        # 当传入的l1.next也就是当前的新l1为None时也无需与l2比较，返回l2值
        if not l1:
            return l2
        
				# 递归
				# l1和l2比大小 当l1的值小于等于l2的值时，l1成为当前最小值，mergeTwoLists()实际上就是l1、l2比大小的函数，所以传入l1.next与l2进行比较，返回两者之间的最小值。因为递归回溯的值是对l1.next的赋值，所以最后返回的也是l1节点。
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # 当l1大于l2时，l2成为当前最小值，因此传入l2.next与l1进行比较，将两者之间的最小值赋值给l2.next
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2print('hello world')