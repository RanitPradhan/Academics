"""
OOP || Lab sheet 3 || Ranit Pradhan || AM.EN.U4ELC19028
"""

class student(object):     
    def __init__(self, name = "Ranit Pradhan", age = 20, fathers_name = "Biswajit Pradhan", phone_num = 9352618795, roll = 28):
        self.info ={     
            "roll number": roll,
            "name" : name,
            "age": age,
            "father's name": fathers_name,
            "phone_number": phone_num
        }

    def display_info(self):
        print(self.info)


students = [student(roll = i) for i in range(5)]

class school(object):
    def __init__(self, students):
        self.student1 = students[0]
        self.student2 = students[1]
        self._student3 = students[2]
        self._student4 = students[3]
        self._student5 = students[4]

s = school(students)
s.student1.display_info()
s.student2.display_info()
