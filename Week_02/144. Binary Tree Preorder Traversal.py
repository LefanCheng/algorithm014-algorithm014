```python
# iterative 迭代解法 参考94.Binary Tree Inorder Traversal中序遍历栈解法，仅调换顺序
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                # preorder: root - left - right, in stack: right - left - root;
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res
```

```python
# 标准递归解法
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, root):
        # base case
        if not root:
            return None
        
        # recursion: root - left - right
        self.res.append(root.val)
        self.helper(root.left)
        self.helper(root.right)
```