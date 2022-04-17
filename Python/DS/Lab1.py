sub=["Physics","Math","Chemistry"]

def arr_append():
    sub.append("English")
    print("\n")
    print("Using append():------------>",sub) #"English" is added to the Array 
    print("\n",50*"-","\n")

def arr_pop():
    sub.pop(2) # POP of 3rd element
    print("Using pop():------------>",sub) 
    print("\n",50*"-","\n")

def arr_index():
    arr=sub.index("Math") # Index of "Math" in the array
    print("Using index():------------>",arr)
    print("\n",50*"-","\n")

def arr_insert():
    sub.insert(1,"Biology") # Inserting "Biology"
    print("Using insert():------------>",sub)
    print("\n",50*"-","\n")

def arr_sort():
    sub.sort() # Sorting the array elements
    print("Using sort():------------>",sub)
    print("\n",50*"-","\n")

def arr_reverse():
    sub.reverse() # Reverse the array
    print("Using reverse():------------>",sub)
    print("\n")

arr_append()
arr_pop()
arr_index()
arr_insert()
arr_sort()
arr_reverse()