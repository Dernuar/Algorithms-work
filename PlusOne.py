class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = digits
        fin = 0
        ans = []

        for i in range(len(n)):
         fin += n[-(i + 1)] * 10 ** i
        fin += 1

        for i in range(len(str(fin))):
           ans.append(int(str(fin)[i]))


        return ans
