n1=input("Enter the name of student_1: ")
n2=input("Enter the name of student_2: ")
n3=input("Enter the name of student_3: ")
n4=input("Enter the name of student_4: ")
class Student:
    def __init__(self,n,**m):
        self.name=n
        self.marks=m

    def display(self):
        print("Hi",self.name)
        print("Your marks", self.marks)

s1= Student(n1,Physics=95,Chemistry=90,Math=100,English=80, Biology=90)
s1.display()


s2= Student(n2,Physics=90,Chemistry=90,Math=95,English=85,Biology=80)
s2.display()


s3= Student(n3,Physics=100,Chemistry=90,Math=90,English=90,Biology=75)
s3.display()


s4= Student(n4,Physics=95,Chemistry=99,Math=92,English=86,Biology=95)
s4.display()


