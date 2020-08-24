Given an n-ary tree, return the level order traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Example 1:**

![https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
```

**Example 2:**

![https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
```

**Constraints:**

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

```python
# Queue层次遍历解法，参考二叉树层次遍历：
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from queue import Queue

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # print(root.val)
        if not root:
            return
        
        res = []        
        que = Queue()
        que.put(root)
        
        while not que.empty():
            temp = []
            n = que.qsize()
            
            for i in range(n):
                cur = que.get()
                temp.append(cur.val)
                
                if cur.children:
                    for child in cur.children:
                        que.put(child)
                        
            res.append(temp)
            
        return res
            
# 二叉树/Binary Tree 分层遍历/Level Order Traversal
def breadth_first_traverse_by_level(root):
    # base case 当root为None时函数结束
    if not root:
        return

    que = Queue(maxsize=0) # 声明一个空队列 size无限制
    que.put(root) # 将根结点放入队列

    # 当队列非空时 每次从队列中取一个元素出来
    while not que.empty():
        n = que.qsize() # 获取当前队列元素数量
        # 分层遍历与普通遍历区别 进行长度为n的for循环
        for i in range(n):
            cur = que.get() #每一次取出队列的头部
            print(cur.val, end=' ')
            # 如果左孩子存在 将左孩子放入队列当中
            if cur.left: 
                que.put(cur.left)
            # 如果右孩子存在 将右孩子放入队列当中
            if cur.right:
                que.put(cur.right)
        print()
```