n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
def avg(student_marks):
    for i,v in student_marks.items():
        if i == query_name:
            a=sum(v)/len(v)
            print(f"{a:.2f}")
avg(student_marks)