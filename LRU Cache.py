class Node:
    def __init__(self,key=0,val=0,next=None,prev=None):
        self.val=val
        self.key=key        
        self.next=next
        self.prev=prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.hashMap={}
        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
    

    def remove(self,node):
        next=node.next
        prev=node.prev
        next.prev=prev
        prev.next=next
    

    def insert(self,node):
        next=self.right
        prev=self.right.prev
        prev.next=node
        next.prev=node
        node.next=next
        node.prev=prev


    def get(self, key: int) -> int:
        if key in self.hashMap:
             node=self.hashMap[key]
             self.remove(node)
             self.insert(node)
             return node.val
        else:
            return -1
       


    def put(self, key: int, value: int) -> None:
        newNode=Node(key,value)
        if key in self.hashMap:
            node=self.hashMap[key]
            self.remove(node)
            del self.hashMap[key]
        if self.cap<=len(self.hashMap):
            node=self.left.next
            self.remove(node)
            del self.hashMap[node.key]
        self.hashMap[key]=newNode
        self.insert(newNode)









        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
