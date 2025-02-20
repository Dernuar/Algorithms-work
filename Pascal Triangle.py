class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = []
        row = numRows

        for i in range(row):
            x = [1] * (i + 1)
            for j in range(1, i):
                x[j] = n[i - 1][j - 1] + n[i - 1][j]
                n.append(x)
        return n