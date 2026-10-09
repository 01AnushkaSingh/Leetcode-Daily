class Node:
    def __init__(self,key:int,value:int):
        self.key,self.value = key ,value
        self.prev = None
        self.next= None 

class LRUCache:
    def __init__(self,capacity):
        self.cap=capacity
        self.cache={}
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next=self.right 
        self.right.prev=self.left 

    def remove(self,node):
        prev,nxt=node.prev,node.next 
        prev.next,nxt.prev=nxt,prev


    def insert(self,node):
        prev, nxt =self.right.prev,self.right
        prev.next = nxt.prev=node 
        node.next,node.prev=nxt,prev

    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)