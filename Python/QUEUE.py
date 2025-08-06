                    # A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
                    # The first person to stand in line is also the first who can pay and leave the supermarket.

                    # Enqueue: Adds a new element to the queue.
                    # Dequeue: Removes and returns the first (front) element from the queue.
                    # Peek: Returns the first element in the queue.
                    # isEmpty: Checks if the queue is empty.
                    # Size: Finds the number of elements in the queue.


queue = []
# Enqueue
queue.append('11')
queue.append('5')
queue.append('76')
queue.append('104')
queue.append('43')
queue.append('27')
queue.append('12')
queue.append('61')
queue.append('83')
queue.append('75')
queue.append('99')

print("QUEUE => ",queue)
# Peek
front_element = queue[0]
print("QUEUE front elemnt is => ",front_element)
# Dequeue
pop = queue.pop(0)
print("QUEUE poped element is => ",pop)
# Is empty
isempty = not bool (queue)
print("QUEUE is empty => ",isempty)
# Size
print("QUEUE len is => ",len(queue))



                    # Class and object methods.



class Queue:
    
    def __init__(self):
        self.queue= []
        
    def enqueue(self,element):
        self.queue.append(element) 
        
    def dequeue(self):
        return self.queue.pop(0)   
    
    def peek(self):
        return self.queue[0] 
    
    def isempty(self):
        return len(self.queue) == 0
        
    def size(self):
        return len(self.queue)
    
    
q1 = Queue() 
q1.enqueue('37')
q1.enqueue('65')
q1.enqueue('14')
q1.enqueue('92')
q1.enqueue('45')
q1.enqueue('63')
q1.enqueue('29')
q1.enqueue('70')
q1.enqueue('81')

print("QUEUE Enqueue Elements =>",q1.queue)
print("QUEUE Peeked Element =>",q1.peek())
print("QUEUE Pooped Elements =>",q1.dequeue())
print("QUEUE Pooped Elements =>",q1.dequeue())
print("QUEUE Enqueue Elements =>",q1.queue)
print("QUEUE is Empty =>",q1.isempty())
print("QUEUE Size is =>",q1.size())
q1.enqueue('100')
q1.enqueue('126')
print("QUEUE Enqueue Elements =>",q1.queue)

