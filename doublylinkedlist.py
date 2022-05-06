


class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
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
            self.head.next=node
            return
        curr_node = self.head.next

        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node
        node.prev = curr_node
    
    def prepend(self, data):
        frist_node = self.head

        if frist_node is None:
            return