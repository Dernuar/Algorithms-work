class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start, end, index = 0, len(nums) - 1, 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                start = index = mid + 1
            else:
                end = mid - 1
                index = mid

        return index