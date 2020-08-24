Given a non-empty array of integers, return the **k** most frequent elements.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Note:**

- You may assume  is always valid, 1 ≤  ≤ number of unique elements.
- Your algorithm's time complexity **must be** better than O( log ), where  is the array's size.
- It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
- You can return the answer in any order.

```python
# 小顶堆+哈希表 解法，速度很慢，需要一个更快的解法
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        # from collections import Counter
        # dic = Counter(nums)
        
        heap = []
        for num, freq in dic.items():
            if len(heap) == k:
                if heap[0][0] < freq:
                    # (freq, num)可以但(num, freq)却不可以，为什么？在heapq中二叉堆节点以元组存储依据什么比大小？是以tuple索引为0的值排序吗，即(freq, num)中的freq吗？
                    heapq.heapreplace(heap, (freq, num))
            else:
                heapq.heappush(heap, (freq, num))
        
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return res
```