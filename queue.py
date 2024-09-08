class queue:
  def __init__(self):
    self.list=[]
    
  def enqueue(self,item):
    self.list.append(item)
    
  def dequeue(self):
    if len(self.list)!=0:
      self.list.pop(0)
    else:
      return "queue is empty"
            
        
queue = queue()
queue.enqueue('1')
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
print(queue.list)