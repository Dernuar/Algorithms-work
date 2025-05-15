class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        answer = []

        for start, end in intervals:           
            if not(answer) or answer[-1][1] < start:
                answer.append([start,end])
            else:
                answer[-1][1] = max(answer[-1][1], end)
                
        return answer  