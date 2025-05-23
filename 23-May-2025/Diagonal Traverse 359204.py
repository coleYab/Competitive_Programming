# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])
        ans= []
        for entry in d.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans