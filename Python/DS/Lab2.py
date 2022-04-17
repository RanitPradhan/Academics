class Mathematics_marks(object):    
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def print_array(self):
        for i in range(0, len(self.items)-1):    
            print (self.items[i], end = ", ")
        print(self.items[i+1])


m=Mathematics_marks()
x=0
print("Enter marks: ")
while x<10:
    a=int(input())
    if x<5:
        m.enqueue(a)
    else:
        m.push(a)
    if x==4:
        print("Mathematics marks after enqueuing ")
        m.print_array()
        print("Enter marks to append to array as stack")
    if x==9:
        print("Mathematics marks after appending ")
        m.print_array()
    x=x+1
     
x=0
print("Mathematics marks by using pop ")
while x<10:
    print(m.pop())
    x=x+1
