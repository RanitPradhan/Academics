result = None
class zero_div_error():
    x = int(input("Number 1: "))
    y = int(input("Number 2: "))

    try:
        result = x/y
    except ArithmeticError as e:
        print("ArithmeticError: Found !! : ",type(e))
    else:
        print("No Error found :)")
    print("Result = ",result)
    print("\n---New Line---\n")

class type_error():
    x = input("Number 1: ")
    y = input("Number 2: ")

    try:
        result = x/y
    except TypeError as e:
        print("TypeError: Found !! : ",type(e))
    else:
        print("No Error found :)")
   
    print("Result = ",result)
    print("\n---New Line---\n")

class name_error():

    try:
        print(name)
    except NameError as e:
        print("NameError: Found !! : ",type(e))
    else:
        print("No Error found :)")
    print("Result = ",result)
    print("\n---New Line---\n")

class overflow_error():
    x = input("Number 1: ")
    try:
        import math
        print(math.exp(2000))
    except OverflowError as e:
        print("OverflowError: Found !! : ",type(e))
    else:
        print("No Error found :)")
    print("Result = ",result)
zero_div_error()
type_error()
name_error()
overflow_error()
    
