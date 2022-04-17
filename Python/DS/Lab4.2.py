#Doubly LinkedList
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DbLinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            self.head = new_node

    def insert(self,prev_node,new_value):
        if prev_node is None:
            print("Given previous node can't be NULL !!")
            return
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next:
            new_node.next.prev = new_node

    def append(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while True:
            if last.next == None:
                last.next = new_node
                new_node.prev = last
                return
            last = last.next
        
    def printLL(self,node):
        print("\nIn forward direction")
        while node:
            print((node.value))
            node = node.next
    
    def delete_node(self,node,dlt):
        while node:
            if dlt==node.value:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next

lnlist= DbLinkedList()

lnlist.append("Darjeeling")
lnlist.printLL(lnlist.head)

lnlist.push("Sikkim")
lnlist.push("Kedarnath")
lnlist.push("Manali")
lnlist.push("Agra")
lnlist.push("Ladakh")
lnlist.push("Goa")

lnlist.append("Munnar")

print("\nBefore adding the place created Doubly LL")
lnlist.printLL(lnlist.head)

lnlist.insert(lnlist.head.next,"J&K")
print("\nAfter adding the place to Doubly LL")
lnlist.printLL(lnlist.head)

lnlist.delete_node(lnlist.head,"Manali")
print("\nAfter deleting the place from the DLL")
lnlist.printLL(lnlist.head)

lnlist.head.value = "Rajasthan"
lnlist.printLL(lnlist.head)