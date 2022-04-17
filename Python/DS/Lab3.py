class Physics_marks(object):
    def __init__(self):
        self.items=[]
    
    def add_rear(self,item):
        self.items.append(item)
    
    def add_front(self,item):
        self.items.insert(0,item)

    def remove_rear(self):
        return self.items.pop()
    
    def remove_front(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

    def print_array(self):
        for i in range(0, len(self.items)-1):    
            print (self.items[i], end = ", ")
        print(self.items[i+1])


p=Physics_marks()
x=0
print("Enter marks to append to dequeue in rear")
while x<6:
    a=int(input())
    if x<3:
        p.add_rear(a)
    else:
        p.add_front(a)
    x=x+1
    if x==3:
        print("Physics marks after appending it in rear ")
        p.print_array()
        print("Enter marks to append to dequeue at front")
    if x==6:
        print("Physics marks after appending it from front ")
        p.print_array()
x=0
print("Physics marks removing from rear")
while x<6:
    if x<3:
        print(p.remove_rear())
    else:
        print(p.remove_front())
    x=x+1
    if x==3:
        print("Physics marks removing from front")
