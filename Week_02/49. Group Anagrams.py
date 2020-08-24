**49. Group Anagrams**

Given an array of strings, group anagrams together.

**Example:**

```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note:**

- All inputs will be in lowercase.
- The order of your output does not matter.

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Anagrams 指的是组成字母即出现次数相同的单词 其排序后应当相等 由于哈希表键值不可变 我们使用由排好序的单词tuple作为键 Anagrams组成的list为值 最后返回值作为答案
        dic = {}
        # 利用dic.get()特性实现Anagrams list作为值
        for word in strs:
            key = tuple(sorted(word))
            dic[key] = dic.get(key, []) + [word]
        return dic.values()

# 时间复杂度O(n)
# 空间复杂度O(..)
```