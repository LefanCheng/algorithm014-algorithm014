Week 2 学习笔记

# 哈希表、映射、集合

# 树、二叉树、二叉搜索树

# 堆heap和二叉堆Binary Heap

## Heap 堆

Heap 堆 是一种可以迅速找到一堆数中**最大**或者**最小**值的数据结构；

将根节点最大的堆叫做大顶堆或大跟堆，根节点最小的堆叫做小顶堆或小根堆。常见的堆有二叉堆，斐波那契堆等。

假设是大顶堆，则常见操作(API):

- find-max: $O(1)$
- delete-max: $O(logn)$
- insert(create): $O(logN)$ or $O(1)$

[不同实现的比较](https://en.wikipedia.org/wiki/Heap_(data_structure))

## 二叉堆

二叉堆通过**完全二叉树**来实现，即除了叶子节点一层可以不是丰满状态，其上的每一层都是丰满的（注意：不是二叉搜索树）

二叉堆（大顶）它满足下列性质：

- 是一颗完全二叉树
- 树中任意节点的值总是 ≥ 其子节点的值

    ![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.46.00_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.46.00_PM.png)

    一维数组：[110, 100, 90, 40, 80, 20, 60, 10, 30, 50, 70]

二叉堆一般通过“数组”来实现，假设“第一个元素”在数组中的索引为0的话，则父节点和子节点的位置关系如下：

1. 索引为i的左孩子的索引是 $(2 \cdot i+1)$
2. 索引为i的右孩子的索引是 $(2 \cdot i+2)$
3. 索引为i的父孩子的索引是 $floor((i-1)/2)$  ( i 减 1 除以 2 然后向下取整数)
4. 根节点（顶堆元素）是：`a[0]`

### Insert 插入操作

1. 新元素一律先插入到堆的尾部
2. 依次向上调整整个堆的结构（一直到根即可）- HeapifyUp

1. 时间复杂度为$O(logn)$

    ![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.57.47_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.57.47_PM.png)

    Step 1 将值为85的节点添加到二叉堆中

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.58.06_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.58.06_PM.png)

Step 3 85大于其父节点40，二叉堆中任意节点的值总是 ≥ 其子节点的值，因此将其与父节点互换

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.57.57_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.57.57_PM.png)

Step 2 为不破坏二叉堆结构，将新节点先插入堆的末尾[...10, 50, 85]

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.58.15_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_4.58.15_PM.png)

Step 4 同理再次与其父节点80互换 插入完毕

### Delete Max 删除堆顶操作

1. 将堆尾元素替换到顶部（即堆顶被替换删除）
2. 依次从根部向下调整整个堆的结构（一直到堆尾即可）- HeapifyDown

时间复杂度：$O(logn)$

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_5.04.44_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_5.04.44_PM.png)

注意：二叉堆是堆（优先队列priority_queue）的一种常见且简单的实现，但并非最优的实现，如下图所示。工程中较少用二叉堆，常用严格斐波那契堆。

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_5.17.55_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-23_at_5.17.55_PM.png)

```python
# 二叉堆 Binary Heap Python实现
import sys 
class BinaryHeap: 
  
    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.Heap = [0]*(self.capacity + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    def parent(self, pos): 
        return pos//2
  
    def leftChild(self, pos): 
        return 2 * pos 
  
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
  
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    def heapifyDown(self, pos): 
  
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.heapifyDown(self.leftChild(pos)) 
  
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.heapifyDown(self.rightChild(pos)) 
  
    def insert(self, element): 
        if self.size >= self.capacity : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
   
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.heapifyDown(pos) 
  
    def delete(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.heapifyDown(self.FRONT) 
        return popped 
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self): 
        return self.size == self.capacity
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = BinaryHeap(5)
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
  
    minHeap.Print() 
    print("The Min val is " + str(minHeap.delete()))
```

# 图