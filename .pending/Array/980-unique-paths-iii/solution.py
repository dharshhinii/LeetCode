class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        global c
        n=len(grid)
        m=len(grid[0])
        sol=[[0]*m for _ in range(n)]
        nc=s=ss=0
        d=[(-1,0),(0,-1),(1,0),(0,1)]
        for ii in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[ii][k]!=-1:
                    nc+=1
                if grid[ii][k]==1:
                    s,ss=ii,k
        sp=1
        c=0
        def find(i,j,sol,sp):
            global c
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==-1 or sol[i][j]==1:
                return

            if grid[i][j]==2:
                if sp==nc:
                    c+=1
                return
            sol[i][j]=1
            for x,y in d:
                find(i+x,j+y,sol,sp+1)
            sol[i][j]=0
            return
        find(s,ss,sol,sp)
        return c

