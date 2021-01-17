class CircularQueue:
  

  def __init__(self, maxSize):
    self.queue = list()
    # user input value for maxSize
    self.maxSize = maxSize
    self.head = 0
    self.tail = 0

  def enqueue(self, data):
    
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")
    else:
      
      self.queue.append(data)
      # increment the tail pointer
      self.tail = (self.tail+1) % self.maxSize
      return True

  def dequeue(self):
    
    if self.size() == 0:
      return("Queue is empty!")
    else:
     
      data = self.queue[self.head]
 
      self.head = (self.head+1) % self.maxSize
      return data
  
  def size(self):
    if self.tail >= self.head:
      qSize = self.tail - self.head
    else:
      qSize = self.maxSize - (self.head - self.tail)
 
    return qSize

size = input("Enter the size of the Circular Queue: ")
q = CircularQueue(int(size))


print(q.dequeue(10))
print(q.head)
print(q.tail)
print()
print()
