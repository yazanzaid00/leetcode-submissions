class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r, t, b = 0 , len(matrix[0]) - 1, 0, len(matrix) - 1
        while l <= r and t <= b:
            for j in range(l, r + 1):
                res.append(matrix[t][j])
            t += 1
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r or t > b:
                break
            for j in range(r, l - 1, -1):
                res.append(matrix[b][j])
            b -= 1
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res