**242. Valid Anagram**

Given two strings *s* and *t* , write a function to determine if *t* is an anagram of *s*.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

**Note:**You may assume the string contains only lowercase alphabets.

**Follow up:**What if the inputs contain unicode characters? How would you adapt your solution to such case?

```python
# 解法1：哈希表，时间O(n),空间O(1)因只有26个字母keys
class Solution:
    # 判断t是否由s重新排序组成的
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果两个字符串长度不同，特判直接返回
        if len(s) != len(t):
            return False
        # 哈希表储存字符与对应出现次数
        dic = {}
        # 同时遍历两个字符串，每次在s中出现的字符就在dic中的对应字符次数+1，如果不存在就赋值对应字符次数为1，而与此同时每次在t中出现的字符则-1
        for ch1,ch2 in zip(s,t):
            dic[ch1] = dic.get(ch1, 0) + 1
            dic[ch2] = dic.get(ch2, 0) - 1
        # 最后如果遍历哈希表，如果有值不为0，则说明t不是由s重新排序组成的，False
        for key in dic:
            if dic[key] != 0:
                return False
        
        return True
# 解法2：排序，O(nlogn),O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

```

[题解](https://leetcode-cn.com/problems/valid-anagram/solution/hua-jie-suan-fa-242-you-xiao-de-zi-mu-yi-wei-ci-by/)

解题方案
思路
标签：哈希映射
首先判断两个字符串长度是否相等，不相等则直接返回 false
若相等，则初始化 26 个字母哈希表，遍历字符串 s 和 t
s 负责在对应位置增加，t 负责在对应位置减少
如果哈希表的值都为 0，则二者是字母异位词