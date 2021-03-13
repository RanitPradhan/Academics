class school:
    def __init__ (self,students,average,highest,lowest):
        self.students=students
        self.average=average
        self.highest=highest
        self.lowest=lowest

    def __ge__ (self,other):
        return self.S1>=self.S2
    def __eq__ (self,other):
        return self.S1==self.S2

S1=school(10,70,80,60)
S2=school(10,80,80,50)
print("{Comparing Number Of Students Of Two Divisons}")
if (S1.students>=S2.students):
    if (S1.students==S2.students):
        print("S1 and S2 has equal number of students")
    else:
        print("S1 has more number of students ")
else:
    print("S1 has more number of students ")
print("\n{Comparing Average Marks Of 3 subjects Of Two Divisons}")
if (S1.average>=S2.average):
    if (S1.average==S2.average):
        print("S1 and S2 has equal Average")
    else:
        print("S1 has more Average ")
else:
    print("S2 has more Average ")
print("\n{Comparing Highest Marks Of Two Divisons}")
if (S1.highest>=S2.highest):
    if (S1.highest==S2.highest):
        print("S1 and S2 has equal Highest Marks")
    else:
        print("S1 has highest marks")
else:
    print("S2 has highest marks")
print("\n{Comparing Lowest Marks Of Two Divisons}")
if (S1.lowest>=S2.lowest):
    if (S1.lowest==S2.lowest):
        print("S1 and S2 has equal Lowest Marks")
    else:
        print("S2 has Lowest marks")
else:
    print("S1 has Lowest marks")
