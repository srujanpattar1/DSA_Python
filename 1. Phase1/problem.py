## print("Srujan")
# print("Name: Chintu")
# print(5+5) #10
# print("5+5") #5+5
# print(5+"5") #error, bcz different data types

# x=10
# print(x, type(x))

# x=20
# print(x)
# y=x
# print(y)

# Name="Srujan"
# Age=21
# College="NMAMIT"
# Branch="CSE"
# Goal="AI Engineer"

# print(f"Name: {Name}")
# print(f"Age: {Age}")
# print(f"College: {College}")
# print(f"Branch: {Branch}")
# print(f"Goal: {Goal}")

# x="9.9"
# print(int(float(x))) #first 9.9 is conv into float, then only fractional part of float is printed

# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #this will produce 3.33333
# print(a%b)

# age=90
# eligible=age>18
# print(eligible)

# x = 5
# x += 3
# x *= 2
# x -= 4
# print(x)

# print(-3.5 > -4)

# print("srujan", "loves", "python", sep="❤️")
# print("srujan", end="!@!")

# a=int(input("Enter a: "))
# b=int(input("Enter a: "))
# print("Sum: ", a+b)
# print("Difference: ", a-b)
# print("Product: ", a*b)
# print("Quotient: ", a/b)

# name="SrujanPattar"
# print(name.startswith("S"))
# print(name.endswith("s"))
# print(name.find("Pattar"))

## Mini Project: Student Marks Calculator
## Build a program that:
## 1. Takes the student's name
## 2. Takes marks for 3 subjects
## 3. Calculates total marks
## 4. Calculates average
## 5. Displays the student's name, total and average
student_name=input("Enter the student name: ")
subject1=int(input("Enter the marks of subject1"))
subject2=int(input("Enter the marks of subject2"))
subject3=int(input("Enter the marks of subject3"))
total_marks=subject1+subject2+subject3
avg_marks=(total_marks)/3
print("Student name: ", student_name)
print("Total marks: ", total_marks)
print("Avg marks: ", avg_marks)