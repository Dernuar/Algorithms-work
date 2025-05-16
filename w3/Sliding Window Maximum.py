class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n, ans = [], []
        for i in range(0,len(nums)):
            heappush(n,(-nums[i],i))
            while n[0][1]<=i-k: heappop(n)
            if i>=k-1: ans.append(-n[0][0])
        return ans