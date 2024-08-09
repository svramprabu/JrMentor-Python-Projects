student_name = input("enter name:")
total=0
for i in range(1,6):
    student_marks = int(input("marks:"))
    total += student_marks
print(student_name,"'s marks:",total)