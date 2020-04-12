class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        m = len(grid)
        if m == 0:
            return count
        
        
        
        n = len(grid[0])
        
            
        def merge( i , j ) -> int :
            # print(grid)
            if i >= m or j >= n or i < 0 or j < 0:
                return
            else : 
                # print( i , j )
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    merge(  i+1 , j )
                    merge(  i , j+1 )
                    merge(  i-1 , j )
                    merge(  i , j-1 )               
                
    
        for i in range( m ) :
            for j in range( n ) :
                if grid[i][j] == '1':
                    merge( i , j )
                    count+=1
        return count
