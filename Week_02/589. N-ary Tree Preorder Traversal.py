Given an n-ary tree, return the preorder traversal of its nodes' values.

*Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*

**Follow up:**

Recursive solution is trivial, could you do it iteratively?

**Example 1:**

![https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

```

**Example 2:**

![https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png](https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png)

```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

```

**Constraints:**

- The height of the n-ary tree is less than or equal to `1000`
- The total number of nodes is between `[0, 10^4]`

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 前序遍历：根-左-右
# 标准递归解法：
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root:
            return []
        
        self.res.append(root.val)
        for child in root.children:
            self.dfs(child)

# 迭代解法:
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        
        while stack:
            temp = stack.pop()
            # 先序遍历: 先遍历根节点 - 再遍历孩子节点
            res.append(temp.val)
            # 如果temp即当前栈顶弹出节点没有孩子节点，则进入下一循环弹出下一栈顶元素；
            if temp.children:
                # 栈后进先出，从最左孩子开始往右遍历，因此从最右孩子开始压栈；此处注意，先序遍历递归时，root其func被call的时候就append进res了，而迭代/栈解法是先压入栈，弹出的时候再append进res，因此顺序不同（我的理解）；
                for child in temp.children[::-1]:
                    stack.append(child)
        return res
```