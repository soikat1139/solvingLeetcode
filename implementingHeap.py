#declaring heap class

class Heap:
  def __init__(self):
    self.heap=[0]
  def push(self,val):
    self.heap.append(val)
    i=len(self.heap)-1
    while self.heap[i]<self.heap[i//2]:
      temp=self.heap[i]
      self.heap[i]=self.heap[i//2]
      self.heap[i//2]=temp
      i=i//2
  def pop():
    if len(self.heap)==1:
      return None
    if len(self.heap)==2:
      return self.heap.pop()
      
