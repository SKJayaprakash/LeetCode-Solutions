class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)
        
        if size <= 0:
            return 0
        ans=0
        left_max = [height[0]] + [0 for i in range(size-1)]
        right_max = [ 0 for i in range(size-1)]+[height[size-1]]
        
        for i in range(1,size):
            left_max[i] = max(left_max[i-1],height[i])
        
        for i in range(size-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i])
            
        for i in range(size):
            ans += min(left_max[i],right_max[i])-height[i]
            
        return ans
