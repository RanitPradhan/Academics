#Singly LinkedList
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
class SnLinkedList:
    def __init__(self ,head):
        self.node=head
        print(self.node.data,end=" ")
        self.node=self.node.next
        while self.node:
            print("--> "+self.node.data,end=" ")
            self.node=self.node.next
        print()

head = Node("Darjeeling");n1 = Node("Sikkim");n2 = Node("Kedarnath") ;n3 = Node("Manali") 
n4 = Node("Agra") ;n5 = Node("Ladakh") ;n6 = Node("Goa") ;n7 = Node("Munnar") 
head.next=n1 ; n1.next=n2 ; n2.next=n3 ; n3.next=n4 ; n4.next=n5
n5.next=n6 ; n6.next=n7
print("------Initial Linked List------")
display=SnLinkedList(head) 
print()
print("------Linked List after changing a destination------")
n2.data="Goa"
display.__init__(head)
print()
print("------Linked List after Inserting a new node------")
n8=Node("J&K");n7.next=n8
display.__init__(head)
print()
print("------Linked List after deleting a node------")
n7.next=None
display.__init__(head)