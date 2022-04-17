def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0] = newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]
k=BinaryTree(2)
insertLeft(k,2)
insertLeft(k,7)
left=getLeftChild(k)
insertRight(left,6)
Ri=getRightChild(left)
insertLeft(Ri,5)
insertRight(Ri,11)
insertRight(k,9)
insertRight(k,5)
Right=getRightChild(k)
Right1=getRightChild(Right)
insertLeft(Right1,4)
print(k)