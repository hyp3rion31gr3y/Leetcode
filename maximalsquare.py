class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r=len(matrix)
        c=len(matrix[0])
        ans=0
        for i in range(r):
            for j in range(c):
                matrix[i][j]=int(matrix[i][j])
                if(matrix[i][j]==0):
                    continue
                if(i==0 or j==0):
                    ans=max(ans,matrix[i][j])
                    continue
                matrix[i][j]=1+min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                ans=max(ans,matrix[i][j])
        return ans*ans
