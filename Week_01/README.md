# 极客大学算法训练营

# 高效学习方法

1. 三分理解七分练习 视频1.5 ~ 2.0 倍数播放 难点暂停与反复播放
2. 摒弃死磕式的非职业化旧习惯 敢于死记硬背高票代码优质题解（+理解）且不懒于看高手代码 不要死磕AC
3. 最佳方式是5分钟想不出直接看题解或高票代码 变为自己的东西 借势而起 千万不要使用自己半小时死磕这种素人低效方式
4. “五毒神掌” - 遍数是关键 每道做过的题保证过过五遍
5. 一定要避免LeetCode只做一遍的**最大误区**

# 数据结构与算法总览

课程学习注意三点：注重预习 - 上课前查看课件、课堂当中互动跟着一起思考回答问题、课后坚持通过切题方法完成

期待效果：对于数据算法机构的理解达到职业顶尖级别、一线互联网公司面试、LeetCode 300+积累

职业训练：

- 拆分知识点：脑图&脉络连接 将知识形成树状结构 Elon Musk
- 刻意练习
    - 把基础动作进行分解与反复的训练 基本功是业余与职业的根本区别 核心是过遍数（五毒神掌） 通过对典型题目的不断练习 举一反三 把不同的算法与数据结构过遍树 带来基本功的提升
    - 专项练习缺陷、弱点的题目类型 不爽枯燥就意味着成长
- 反馈
    - 主动式反馈：看LeetCode与Github上的高手代码
    - 被动式反馈：Code Review 高手给你反馈

## 数据结构分为三大块

- 一维数据结构
    - 基础：数组array(string), 链表 linked list
    - 高级：栈Stack、队列Queue、双端队列deque、集合set、映射map (hash or map), etc
- 二维数据结构 一维泛化而来
    - 基础：树tree、图graph
    - 高级 - 主要在树的基础上加了很多特殊判断和约定条件：二叉搜索树 binary search tree (red-black tree, AVL), 堆 heap、并查集 disjoint set、字典树Trie, etc
- 特殊数据结构 用于工程中特定的情景
    - 位运算 Bitwise、布隆过滤器 BloomFilter
    - LRU Cache、其他替换算法

## 算法八点

- 算法三大基石（任何高级的算法数据结构 到了最后都会转换成以下三者之一 把所有知识体系学完后 化繁为简后的根本就是找到算法的重复单元 基于这个重复单元就可以泛化成高级数据结构 最后所有**复杂算法其实就是找重复单元是什么**）
    - If-else, switch -> branch 跳转语句 逻辑切换
    - for, while loop -> iteration 循环
    - 递归 Recursion (Divide & Conquer, Backtrace) 函数自己调用自己
- 基于以上三大基石的五点高级算法
    - 搜索 Search：深度优先搜索 Depth first search，广度优先搜索 Breadth first search，启发式搜索 A*，etc
    - 动态规划 Dynamic Programming
    - 二分查找 Binary Search
    - 贪心 Greedy，排序算法
    - 数学 Math，几何 Geometry
    - 注意：在头脑中回忆上面每种算法的思想和代码模板

制作脑图，范例：

[%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/--4.pdf](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/--4.pdf)

脑图范例

## **刷题技巧**

### 切题四件套 - 四步系统化的题目思考方式

- Clarification 仔细看题与面试官反复沟通确保理解正确
- Possible Solutions 把所有可能的解法过一遍
    - Compare 比较不同解法之间的时空复杂度
    - Optimal 从中找出最优的解法 一般是时间最快
- Coding 多写
- Test Cases 列举测试样例 给面试官有始有终注意正确性的印象

### 五遍刷题法

- 第一遍：
    - **五分钟**读题+思考 基础薄弱最多十五分钟
    - 没有思路不会做的话 直接看解法 注意 多解法 比较解法优劣 （理解学习而非发明创造）
    - 背诵默写 好的解法
- 第二遍：
    - 马上自己写 闭卷考试 开一个浏览器一个空白文件 在里面敲代码 完成后放到LeetCode上提交 Debug直到通过
    - 多种解法比较、体会 优化 领先80、90%比较好
- 第三遍：
    - **二十四小时**之后，再重复做题
    - 不同解法熟练程度不同的话 对不熟悉的解法进行**专项练习**
- 第四遍：
    - 过了**一周**：反复回来练习相同题目 并对弱项进行专项练习
    - 基本上对同类题目很熟练了
- 第五遍：
    - 面试前半\一\两周恢复性训练

目标结果：肌肉式记忆 一看到题目就知道方法一二三是什么 马上可以把代码模板可以写出来

# 训练环境设置、编码技巧与Code Style

电脑设置：

- Mac: iTerm2 + zsh (oh my zsh), Windows: [Microsoft new terminal](https://github.com/microsoft/terminal)
- VSCode; Java: IntelliJ; Python: PyCharm;
- LeetCode plugin (VSCode & IntelliJ & PyCharm)

参考链接

- [第一次使用VS Code时你应该知道的一切配置](https://juejin.im/post/6844903826063884296)
- [VS Code Themes](https://vscodethemes.com/)
- [教你打造一款颜值逆天的VS Code](https://toutiao.io/posts/7w5ixl/preview)
- [酷炫的VS Code毛玻璃效果](https://juejin.im/post/6844903846871842823)

LeetCode：

- [LeetCode-cn.com](http://leetcode-cn.com/) 中国与国际版LeetCode域名差异只在`-cn`
- 五遍练习法的第三第四遍时，一定要去国际版的discuss board上看前三名most votes对应使用语言的回答

指法与小操作：

- `fn + delete` 删除光标右侧
- `option + delete` 删除光标左侧单词
- Google IDE-name top tips/使用技巧

自顶向下的编程方式：

- 来源：[Clean Code](https://markhneedham.com/blog/2008/09/15/clean-code-book-review/)
- 使用类似新闻稿形式将最关键的函数放置在最上面 而子函数放在后面 思考问题时 先思考高层次( 主干 )逻辑 先森林再枝干再叶子
- 案例：[验证回文串](http://leetcode-cn.com/problems/valid-palindrome/)

```java
# 1.先把非字母非数字去掉并且全部小写  2.翻转后进行比较
def isPalindrome(s):
	filteredS = filterNonNumberAndChar(s)
    reversedS = reverseString(filteredS)
    return reversedS.equalsIgnoreCase(filteredS)
  
def filterNonNumberAndChar(s):
  	return s.reverse()
def reverseString(s)
	return s.replaceAlll("[^A-Za-z0-9]", "")
```

# 时间复杂度

- [如何理解算法时间复杂度的表示法](http://www.zhihu.com/question/21387264)
- [wiki：Master theorem](http://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
- [wiki：主定理](http://zh.wikipedia.org/wiki/%E4%B8%BB%E5%AE%9A%E7%90%86)

## Big O notation

O(1): Constant Complexity 常数复杂度

O(log n): Logarithmic Complexity 对数复杂度

O(n): Linear Complexity 线性时间复杂度

O(n^2): N square Complexity 平方

O(n^3): N cubic Complexity 立方

O(2^n): Exponential Growth 指数

O(n!): Factorial 阶乘

不考虑前面的常数系数

直接看函数根据n的不同情况会运行多少次

养成下意识分析时间空间复杂的的习惯 它们的改进可以给公司带来巨大的资源节约 思考最优解

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled.png)

各级别时间复杂度比对

范例：

```java
// 时间复杂度为O(log n) 
// i = 2, 4, 8, 16 ... n为4时函数执行两次 n为8时函数执行三次 ... 函数执行的次数是x=log2n次 2的x次方为n
for (int i = 1; i < n; i = i * 2) {
	System.out.println("Hey, I'm busy looking at: " + i);
}

// 时间复杂度为O(k^n) k为常数 k的n次方 可以理解为2的n次方 是指数级的
// 面试中一定不要这么写 大量冗余计算 “可以加一个缓存把中间结果缓存下来 或者直接用循环来写”
int fib(int n) {
	if (n<2) return n;
	return f(n - 1) + f(n - 2)
}
```

Fibonacci 数列如果如右图与以上的代码直接用递归 每多展开一层 运行的节点数 (也就是执行次数)是上面一层的两倍 层1、2、3、4节点数分别是1、2、4、8 → 最后一层是大概2的n次方个节点

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled%201.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled%201.png)

## Master Theorem 主定理

主定理可用于计算任何分治与递归函数复杂度

递归四种常见情形：

- Binary Search 二分查找 $O(log n)$ 基于有序数列
- Optimal sorted matrix search 有序二维矩阵中的二分查找
    - 二分查找一维数组$O(logn)$ 二维数组$O(n)$
- Binary tree traversal 二分树遍历  $O(n)$
    - 每个节点都访问一次且只访问一次
    - n 代表二叉树的节点总数
        - 同理 图的遍历、DFS、BFS的时间复杂度都是$O(n)$
- Merge sort 归并排序 $O(nlogn)$
    - 所有排序算法最优的时间复杂度就是 $O(nlogn)$

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled%202.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Untitled%202.png)

Master Theorem Application to Common Algorithms

# 空间复杂度

- 数组的长度
- 递归的深度（特殊说明）
- 数组+递归 → 取两者之间的最大值

# 数组、链表、跳表

## 数组 Array

Java, C++:

`int a[100];`

Python:

`list = []`

JavaScript:

`let x = [1, 2, 3]`

Array 底层硬件实现：内存管理器开辟一段连续内存地址并通过其直接访问，这段连续内存访问任意地址时间复杂度都是$O(1)$

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.26.52_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.26.52_AM.png)

内存管理器

[%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/03_---.pdf](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/03_---.pdf)

本课课件

Array 主要问题在于插入与删除元素需要移动大段数组，导致最好最坏时间复杂度为$O(1)$与$O(n)$，平均时间复杂度为$O(n)$ 

Java源码ArrayList 

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.39.50_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.39.50_AM.png)

在Array末尾加入元素，先判断数组size是否足够， 不够的话增加size，之后加入元素并return true 表示添加成功

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.39.13_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.39.13_AM.png)

在index位置加入e，检查上下界，count操作，进行群移操作，ensure capacity，将原地址的起点位置拷贝到目标位置去(index + 1)，然后将data[index]位置置为e

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.44.49_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.44.49_AM.png)

ensureCapacity首先检查当前数组长度，如果长度够什么都不做，如果要求的minimum capacity和当前长度不够，就new一个新的数组，长度为当前长度乘以2，然后把老数组的值拷贝到新数组，返回新数组。因此如果对ArrayList进行大量修改操作的话，会涉及大量array copy，时间效率偏低

## 链表 Linked List

链表可以弥补前面数组的缺点，在修改添加删除操作频繁情况下更加适合

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.51.10_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.51.10_AM.png)

单链表

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.52.22_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.52.22_AM.png)

双向链表 Double Linked List

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.55.09_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_8.55.09_AM.png)

循环链表

```python
# 链表简介：链表是一个由节点构成的列表，属于线性数据结构，在Python中属于自定义结构
# 定义链表节点类
class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None

# 手动创建链表
def build_linkedlist():
    print('Build linked list')
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1

# 遍历以上链表
node_1 = build_linkedlist()
def traverse_above_linked_list(head_node):	
	lis = []
	cur = head_node
	while cur is not None:
		lis.append(cur.val)
		cur = cur.next
	return lis
traverse_result = traverse_above_linked_list(node_1)
	
# 基于ListNode节点类构建一个Linked List类，该类只存储链表头结点，基于该头结点实现增删改查功能
class MyLinkedList:
	def __init__(self):
		self.head = None # 链表头结点代表整个链表

	# 查找 Find：传入下标返回对应值
	def get(self, location):
		cur = self.head
		for i in range(location):
			cur = cur.next
		return cur.val

	# 插入 Insert：传入插入位置下标与插入值
	def add(self, location, val):
		# 头结点插入
		if location > 0:
			pre = self.head
			for i in range(location - 1):
				pre = pre.next
			new_node = ListNode(val)
			new_node.next = pre.next
			pre.next = new_node
		# 中间插入
		elif location == 0:
			new_node = ListNode(val)
			new_node.next = self.head
			self.head = new_node

	# 更新 Update/Set
	def set(self, location, val):
		cur = self.head
		for i in range(location):
			cur = cur.next
		cur.val = val

	# 删除 Delete/Remove
	def remove(self, location):
		# 删除头节点
		if location == 0:
			self.head = self.head.next
		
		# 删除中间节点
		if location > 0:
			pre = self.head
			for i in range(location - 1):
				pre = pre.next
			pre.next = pre.next.next

	# 遍历 Traverse
	def traverse(self):
			cur = self.head
			while cur is not None # 或者 while cur:
				print(cur.val, end=' ')

	# 判断链表是否为空
	def is_empty(self):
			return self.head is None
```

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.21.33_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.21.33_PM.png)

链表头部插入节点

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.22.14_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.22.14_PM.png)

链表中间插入节点

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.25.24_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.25.24_PM.png)

链表节点指向/储存值的地址，next属性指向下一个节点对象地址

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.24.44_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-11_at_9.24.44_PM.png)

删除中间节点

Java中的LinkedList是一个标准的双向链表结构

## 数组与链表时间复杂度

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_9.06.48_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_9.06.48_AM.png)

Array 各项操作时间复杂度

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_9.04.18_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-12_at_9.04.18_AM.png)

Linked List 各项操作时间复杂度

Linked List的增加删除操作不会像Array一样引起整个链表的群移操作，也不需要复制移动元素，因此各项修改操作效率很高为$O(1)$，但不支持随机访问，访问效率低为$O(n)$

## 跳表 - 链表优化

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_7.50.23_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_7.50.23_AM.png)

当且仅当**链表元素有序**时，普通链表可以转化为跳表实现查询时间的大幅优化

> 跳表(skip list)对标的是**平衡树(AVL Tree)**和**二分查找**， 是一种 **插入/删除/搜索 都是 $O(log n)$** 的数据结构。1989 年出现，远晚于前两者。

**一维数据结构要加速通常采用升维变成二维**

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.25.03_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.25.03_AM.png)

添加一级索引：在原始链表基础上每次走两步

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.27.04_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.27.04_AM.png)

添加二级索引：在一级索引基础上每次走两步 在原始链表上每次走四步
例如查询8，先在二级索引走一步到7，此时下一步（假设为14）大于8，于是从7向下进入一级索引，一级索引7的下一个节点9依旧大于8，于是从一级索引向下进入原始链表向后遍历直到大于8的数字，寻找到8，否则8不存在

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.34.07_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.34.07_AM.png)

以此类推，增加多级索引 上图为五级索引

### 跳表查询的时间复杂度分析

跳表查询的时间复杂度为：

$O(logn)$

一级索引节点个数为$\frac{n}{2}$，二级索引节点个数为$\frac{n}{4}$，三级索引节点个数为$\frac{n}{8}$，因此:

 $k$ $$ 级索引节点个数为 $\frac{n}{2^k}$

假设索引有 $h$ 级，最高级的索引有 2 个节点，$\frac{n}{2^h}=2$，从而求得：

索引的高度为：$h = (log_2n) - 1$  $≈$ $logn$

例子：

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.40.57_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.40.57_PM.png)

索引的高度：logn，每层索引遍历的结点个数：3，在跳表中查询任意数据的时间复杂度就是 O(logn)，如上图如果查询原始链表中第八个元素，其时间复杂度为 $log_28$

现实中跳表的形态

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.44.29_PM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.44.29_PM.png)

现实中跳表维护成本较高，元素的增加与删除需要更新索引，时间复杂度从普通链表的$O(1)$变为$O(logn)$；而且各层索引中跳跃的元素个数会如上图一样变得不一致；

### 跳表空间复杂度分析

原始链表大小为 n，每 2 个结点抽 1 个，每层索引的节点数为：

$\frac{n}{2}$$, \frac{n}{4} ,$ $\frac{n}{8}$$, ..., 8, 4, 2$  收敛

原始链表大小为 n，每 3 个结点抽 1 个，每层索引的节点数为：

$\frac{n}{3}$$,\frac{n}{9},$ $\frac{n}{27}$$, ..., 9, 3, 1$  收敛

因为索引的节点数是收敛的，因此求和后空间复杂度都是 

$O(n)$

### 跳表思想：升维思想 + 空间换时间

## 工程中的应用

- LRU Cache - Linked List
    - [简书 - LRU缓存算法](https://www.jianshu.com/p/b1ab4a170c3c)
    - [LeetCode - LRU 缓存机制](http://leetcode-cn.com/problems/lru-cache)
- Redis - Skip List：
    - [跳跃表](http://redisbook.readthedocs.io/en/latest/internal-datastruct/skiplist.html)
    - [为啥 Redis 使用跳表（Skip List）而不是使用 Red-Black？](http://www.zhihu.com/question/20202931)

## 其他参考链接

- [Java 源码分析（ArrayList）](http://developer.classpath.org/doc/java/util/ArrayList-source.html)
- [Linked List 的标准实现代码](http://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/)
- [Linked List 示例代码](http://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/code/LinkedList.java)
- [Java 源码分析（LinkedList）](http://developer.classpath.org/doc/java/util/LinkedList-source.html)

# 待整理知识点

动态规划与分治法没有大的区别

动态规划求解问题特征：

![%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.30.23_AM.png](%E6%9E%81%E5%AE%A2%E5%A4%A7%E5%AD%A6%E7%AE%97%E6%B3%95%E8%AE%AD%E7%BB%83%E8%90%A5%206a075180347b4f0d87ffa9eec9486f73/Screen_Shot_2020-08-13_at_8.30.23_AM.png)

# LeetCode 刷题记录

|Name                                                                   |Tags                          |URL                                                                                                    |遍数 |上次做题时间      |
|-----------------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------|---|------------|
|LintCode 72. Construct Binary Tree from Inorder and Postorder Traversal|Binary Tree, Recursion        |https://www.lintcode.com/problem/construct-binary-tree-from-inorder-and-postorder-traversal/description|2  |Aug 12, 2020|
|70. Climbing Stairs                                                    |Dynamic Programming, Fibonacci|https://leetcode.com/problems/climbing-stairs/                                                         |3  |Aug 12, 2020|
|66. Plus One                                                           |Array                         |https://leetcode.com/problems/plus-one/                                                                |1  |Aug 12, 2020|
|1. Two Sum                                                             |Array, Hash Table             |https://leetcode.com/problems/two-sum/                                                                 |3  |Aug 12, 2020|
|24. Swap Nodes in Pairs                                                |Linked List, Recursion        |https://leetcode.com/problems/swap-nodes-in-pairs/                                                     |1  |Aug 12, 2020|
|21. Merge Two Sorted Lists                                             |Linked List                   |https://leetcode.com/problems/merge-two-sorted-lists/                                                  |1  |Aug 13, 2020|
|283. Move Zeroes                                                       |Array, Two Pointers           |https://leetcode.com/problems/move-zeroes/submissions/                                                 |1  |Aug 15, 2020|
|11. Container With Most Water                                          |Array, Two Pointers           |https://leetcode.com/problems/container-with-most-water/                                               |1  |Aug 15, 2020|
|88. Merge Sorted Array                                                 |Array, Two Pointers           |https://leetcode.com/problems/merge-sorted-array/                                                      |1  |Aug 16, 2020|
|20. Valid Parentheses                                                  |Stack, String                 |https://leetcode.com/problems/valid-parentheses/                                                       |1  |Aug 16, 2020|
