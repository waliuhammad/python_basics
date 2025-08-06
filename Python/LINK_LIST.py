class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
    @staticmethod
    def traverse_print(head):
        current_node = head
        while current_node:
            print(current_node.data, end="->")    
            current_node = current_node.next
        print("Null")   
         
    @staticmethod
    def find_max(head):
        max_val = head.data
        current_node = head.next
        while current_node:
            if current_node.data > max_val:
                max_val = current_node.next
            current_node = current_node.next
        return max_val     
    
    @staticmethod
    def find_min(head):
        min_val = head.data
        current_node = head.next
        while current_node:
            if current_node.data < min_val:
                min_val = current_node.next
            current_node = current_node.next
        return min_val    
    
    
    @staticmethod
    def del_node(head, delnode):
        if head == delnode:
            return head.next
        
        current_node = head
        while current_node and current_node != delnode:
            current_node = current_node.next
            
        if delnode is None:
            return head
        
        current_node.next = current_node.next.next
        return head    
            
    @staticmethod
    def insert_node(head, newnode, position):
        if position == 1:
            newnode.next = head
            return newnode
        
        Current_node = head
        for _ in range(position - 2):
            if Current_node is None:
                break
            Current_node = Current_node.next
            
        newnode.next = Current_node.next
        Current_node.next = newnode
        return head    
    
Node1 = Node(3)    
Node2 = Node(4)
Node3 = Node(5)
Node4 = Node(6)
Node5 = Node(7)
Node6 = Node(8)
Node7 = Node(9)
Node8 = Node(10)
Node9 = Node(11)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8
Node8.next = Node9  


Node1 = Node.insert_node(Node1, Node(2), 1)
Node.traverse_print(Node1)
Node.insert_node(Node1, Node(12), 8)
Node.insert_node(Node1, Node(13), 9)
Node.insert_node(Node1, Node(14), 10)
Node.traverse_print(Node1)
                                                                                              