```python
# 标准递归遍历二叉树
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return None
        
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)
```

```python
# 模拟函数调⽤用栈？栈/颜色解法；前中后序仅顺序差异，实际为通过栈模拟递归；
# [题解](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 白色代表未访问，灰色代表已访问，已访问过的节点在回溯？时添入遍历结果
        WHITE, GRAY = 0, 1
        res = []
        # 将初始的root与其状态/颜色初始化于栈中
        stack = [(WHITE, root)]
        # 当栈不为空时，弹出栈顶元素/节点，如果节点颜色为白色/未访问，即将该节点的右孩子-未访问/白色，该节点-已访问/灰色，与该节点的左孩子-未访问/白色依次推入栈中，注意与递归法顺序相反，因栈后进先出，入栈与出栈顺序相反。每次弹出栈顶节点/元素，即上一节点的左孩子，判断该节点的颜色，白色即循环以上步骤，如果为灰色-已访问过的节点/该子树的根节点，则将其作为遍历结果添加进res中。当遇到叶子节点时，其左右孩子None分别被推入栈中，随后叶子节点的左孩子None被弹出栈顶，if not node判断为True，continue，接下来弹出叶子节点(GRAY, node)，添加进res。当二叉树遍历完毕后，中序遍历中即右子树遍历完毕后，所有栈中元素清空，程序结束，返回res list。
        while stack:
            color, node = stack.pop()
            if not node:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
```