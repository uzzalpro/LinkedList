class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)
    

class Linkedlist:
    def __init__(self):
        self.head = Node()
    
    def __repr__(self) :
        output = []

        curr_node = self.head.next

        while curr_node.next:
            output.append(repr(curr_node.next))
        curr_node.next=curr_node

        return ','.join(output)
    
    def append(self, data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
        curr_node = self.head.next

        while curr_node.next:
            curr_node.next=node
        curr_node=curr_node.next

    def prepend(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def search(self,item):
        curr_node = self.head.next
        while curr_node.nex:
            if curr_node.data==item:
                return curr_node
            curr_node=curr_node.next
        return None

    
    def insert(self, position, item):
        curr_node = self.head.next
        
        while curr_node:
            if curr_node.data==position:
                new_node = Node(item,curr_node.next)
                curr_node.next=new_node
                break
        curr_node=new_node.next
        
    
    def remove(self, item):
        prev_node = self.head
        curr_node = prev_node.next

        while curr_node:
            if curr_node.data == item:
                break
            prev_node=curr_node
            curr_node=curr_node.next

        if curr_node is None:
            return None
        
        if self.head.next==prev_node:
            self.head.next=curr_node.next
        else:
            prev_node.next=curr_node.next
         


    
    




        


    