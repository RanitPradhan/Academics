class Binarytree(object):
    def __init__(self,root):
        self.key=root
        self.leftchild=None
        self.rightchild=None
    def insertleft(self,newnode):
        if self.leftchild==None:
            self.leftchild=Binarytree(newnode)
        else:
            t=Binarytree(newnode)
            t.leftchild=self.leftchild
            self.leftchild=t
    def insertright(self,newnode):
        if self.rightchild==None:
            self.rightchild=Binarytree(newnode)
        else:
            t=Binarytree(newnode)
            t.rightchild=self.rightchild
            self.rightchild=t
    def getright(self):
        return self.rightchild
    def getleft(self):
        return self.leftchild
    def setrootval(self,obj):
        self.key = obj
    def getrootval(self):
        return self.key
r=Binarytree(8)
print('ROOT')
print(r.getrootval())
r.insertleft(3)
print('left of 8')
print(r.getleft().getrootval())
r.insertleft(1)
print('left of 3')
print(r.getleft().getrootval())
r.getleft()
r.insertright(6)
print('right of 3')
print(r.getright().getrootval())
r.getright()
r.insertleft(4)
print('left of 6')
print(r.getleft().getrootval())
r.insertright(7)
print('right of 6')
print(r.getright().getrootval())
r.getrootval()
r.insertright(10)
print('right of 8')
print(r.getright().getrootval())
r.insertright(14)
print('right of 10')
print(r.getright().getrootval())
r.getright()
r.insertleft(13)
print('left of 14')
print(r.getleft().getrootval())



        
        
