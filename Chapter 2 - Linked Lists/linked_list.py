from node import Node
   
class LinkedList:
    def __init__(self, nodes):
        self.head = Node(nodes[0])
        curr = self.head
        for i in range(1, len(nodes)):
            curr.nxt = Node(nodes[i])
            curr = curr.nxt
    def __str__(self):
        n = self.head
        s = ""
        while n != None:
            s += str(n) + " -> "
            n = n.nxt
        s += "None"
        return s
            

def reverse(LL):
    curr = LL.head
    prev = None
    while curr.nxt != None:
        next = curr.nxt
        curr.nxt = prev
        prev = curr
        curr = next
    curr.nxt = prev
    LL.head = curr
    
#lst = None
#for i in range(9,-1,-1):
    #lst = [i,lst]
#print(lst)

#fst, rst = lst 
    
# if __name__ == "__main__":
#     nodes = ["a","b","c","d","e","f"]
#     LL = LinkedList(nodes)