# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 基本情况: [1] -> [1], [1->2->3->4] -> [2->1->4->3], [1->2->3->4->5] -> [2->1->4->3->5]
# 算法三大基石：if else, for/while loop, recursion "化繁为简后的根本就是找到算法的重复单元" 本题的重复单元就是head与head.next，两者进行交换，下一个重复单元就是head.next.next与head.next.next.next，同样两者进行交换
# 基本情况中如果只有一个元素head.next is None，返回head 如果规模是奇数，最后一个元素没有对应的交换元素，那么最后一个元素位置不变
# 
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if not head:
            return None
        if not head.next:
            return head
        # recursion
        sec = head.next
        head.next = head.next.next
        sec.next = head
        head.next = self.swapPairs(head.next)
        return secprint('hello world')