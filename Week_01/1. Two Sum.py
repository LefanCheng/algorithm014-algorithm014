class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # open a dict/hashmap to store appeared idx and val pair 
        dic = {}
        
        # enumerate input nums, if diff in dic, return its idx and cur idx, otherwise append val:idx into dict
        for idx, val in enumerate(nums):
            lookup = target - val
            if lookup in dic:
                return [dic[lookup], idx]
            else:
                dic[val] = idx

# time: O(n)        
# space: heap: using dic worst case O(n), best case O(1)