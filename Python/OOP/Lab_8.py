class school1:
    def __init__ (self,students,highest,ranks,failed,school_rank):
        self.students=students
        self.highest=highest
        self.ranks=ranks
        self.failed=failed
        self.school_rank=school_rank

    def __gr__ (self,other):
        return self.s1>=self.s2
    def __eq__ (self,other):
        return self.s1==self.s2
class school2:
    def __init__ (self,students,highest,ranks,failed,school_rank):
        self.students=students
        self.highest=highest
        self.ranks=ranks
        self.failed=failed
        self.school_rank=school_rank

S1=school1(540,99,64,22,5)
S2=school2(500,95,120,12,3)
print("{..... Comparing Number Of Students Of Two Schools....}")

if S1.students>=S2.students:
    if S1.students==S2.students:
        print("Number Of Students In Both The Schools Are Equal")
    else:
        print("School1 Has More Number Of Students")
else:
    print("      School2 Has More Number Of Students")
print("\n {....Comparing Highest Marks Of Students Of Two Schools....}")

if S1.highest>=S2.highest:
    if S1.highest==S2.highest:
        print("Highest Marks Of Students In Both The Schools Are Equal")
    else:
        print("School1 Has Highest Mark")
else:
    print("School2 Has  Highest Mark")
print("\n{....Comparing Lowest Marks Of Students Of Two Schools.....}")

if S1.ranks>=S2.ranks:
    if S1.ranks==S2.ranks:
           print("Both The Schools Have Equal Number Of Ranks")
    else:
        print("School1 Has More Ranks")
else:
    print("School2 Has More Ranks")
print("\n{....Comparing Number Of Failed Students Of Two Schools.....}")

if S1.failed>=S2.failed:
    if S1.failed==S2.failed:
        print("Both The Schools Have Equal Number Of Failed Students")
    else:
        print("School1 Has More Number Of Failed Students")
else:
    print("School2 Has More Number Of Failed Students")
print("\n{....Comparing Rank Of Two Schools....}")

if S1.school_rank>=S2.school_rank:
    if S1.school_rank==S2.school_rank:
        print("Rank Of Both The Schools Are Equal")
    else:
        print("Rank Of School2 Is Greater Than School1")
else:
    print("Rank Of School1 Is Greater Than School2")