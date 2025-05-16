class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        
        for i, num in enumerate(nums):
            if target - num in ht:
                return [ht[target - num], i]
            ht[num] = i
            
        return []