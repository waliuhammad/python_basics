                    # A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.
                    # Think of it like a stack of pancakes - you can only add or remove pancakes from the top.

                    # Push: Adds a new element on the stack.
                    # Pop: Removes and returns the top element from the stack.
                    # Peek: Returns the top (last) element on the stack.
                    # isEmpty: Checks if the stack is empty.
                    # Size: Finds the number of elements in the stack.
                    
stack = []
stack.append('4')           
stack.append('7')          
stack.append('2')          
stack.append('9')          
 
print("stack =>",stack)

top = stack[-1]
print("stack peek =>",top)

pop = stack.pop()
print("stack pop =>",pop)

pop = stack.pop()
print("stack pop =>",pop)

print("stack after pop =>",stack)

isempty = not bool (stack)
print("stack empty =>",isempty)

print("stack size =>",(len(stack)))



                    # Class and object methods.


class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
       
    def peek(self):
        if self.isempty():
            return "Stack is empty"   
        return self.stack[-1]
       
    def pop(self):
        if self.isempty():
            return "Stack is empty"   
        return self.stack.pop() 
    
    def isempty(self):
        return len(self.stack) == 0
    
    def len(self):
        return len(self.stack)
                   
s = Stack()
s.push('7')     
s.push('6')
s.push('3')
s.push('5')
s.push('9')
s.push('10')
s.push('2')
s.push('8')
s.push('1')

print("stack items =>",s.stack)
print("stack poped =>",s.pop())
print("stack peeked=>",s.peek())
print("stack poped =>",s.pop())
print("stack after pop =>",s.stack)
print("stack =>",s.isempty())
print("stack =>",s.len())
