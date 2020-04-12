class LRUCache:
    
    cache = {}
    capacity = 0
    queue = []

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache :
            self.reorderQueue( key )
            return self.cache.get( key , -1 )
        else :
            return -1
        
    def put(self, key: int, value: int) -> None:
        
        self.cache[key] = value
        if len( self.cache.keys()) > self.capacity :
            self.cache.pop( self.queue.pop(0) )
            
        self.reorderQueue( key )
        
        
        # print(key , self.cache.get( key , -1 ) , self.cache)
        
    def reorderQueue( self , recentlyUsedKey: int) -> int:
        
        if recentlyUsedKey in self.queue:
            
            currentIndex = self.queue.index(recentlyUsedKey)
            # print("In reorder queue method" , currentIndex , self.queue , recentlyUsedKey )
            for i in range( currentIndex , len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue.pop()    
            
        self.queue.append( recentlyUsedKey )
        # print("queue" , self.queue)
         
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
