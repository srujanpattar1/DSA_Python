# # Q1. Personal Information
# # Write a program that stores your:
# # - Name
# # - Age
# # - College
# # - GPA
# # and prints them in a readable format.
# name="srujan"
# age=21
# college="NMAMIT"
# gpa=8.74
# print(f" Name:{name} \n Age:{age} \n College:{college} \n Gpa:{gpa} ")


# # Q2. Take two numbers from the user and print arithmetic operations
# a=int(input("a: "))
# b=int(input("b: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)

# # Q3. Take the user's current age and print after age after 5 and 10yrs
# age1=int(input("Age: "))
# print(f"Age after 5yrs: {age1+5}")
# print(f"Age after 10yrs: {age1+10}")

# # Q4. Calculate perimeter and area of rectangle 
# l=int(input())
# b=int(input())
# print(f"Area: {l*b}")
# print(f"Perimeter: {2*(l+b)}")

# Q5. Take temperature in Celsius and convert it to Fahrenheit.
# c=int(input())
# print(f"{(c*(9/5)+32)} F")

# # Q6. Pos, neg, zero
# x=-10
# if x==0:
#     print("Zero")
# elif x>0:
#     print("Pos")
# else:
#     print("Neg")

# # Q7. Odd Even
# num=int(input())
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# # Q8. Voting eligibility
# age=int(input())
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not eligible")

# #Q9. Largest of two num
# num1=int(input())
# num2=int(input())
# if num1 > num2 :
#     print(f"{num1} is largest")
# elif num1 < num2:
#     print(f"{num2} is largest")
# else:
#     print("both are equal")

# # Q10. Grade calculator
# mark=int(input())
# if mark >= 90 and mark <= 100 :
#    print("A")
# elif mark >= 80 and mark <= 89:
#     print("B")
# elif mark >= 70 and mark <= 79:
#    print("C")
# elif mark >= 60 and mark <= 69:
#    print("D")
# else:
#    print("F")

# # Q11. Print numbers from 1 to 10 using a while loop.
# for i in range(1,11):
#     print(i)

# j=1
# while j<=10:
#     print(j)
#     j+=1

# #Q12. Print all even numbers between 1 and 50.
# for i in range(1,51):
#     if (i%2==0):
#         print(i)
# #or
# for i in range(0,51,2):
#     if(i==0):
#         continue
#     print(i)

# #Q13. Calculate the sum of numbers from 1 to 100.
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# #Q14. Multiplication table
# num=int(input())
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# #Q15. Factorial
# num1=int(input())
# fact=1
# for i in range(num1,0,-1):
#     fact=fact*i
# print(fact)

# #Q16. Pattern pritning
# for i in range(1,6):
#     print(i*"*")
    
# #Q17. Print numbers from 1 to 20, but skip multiples of 3.
# for i in range(1,21):
#     if(i%3==0):
#         continue
#     print(i)

# # Q18. Print: 
# text="Python"
# # 1. First character
# # 2. Last character
# # 3. Third character
# # 4. String in reverse
# print(text[0])
# print(text[-1])
# print(text[2])
# print(text[::-1])

# #Q19. String Slicing
# text ="Programming"
# # 1. "Pro"
# # 2. "gram"
# # 3. Last 4 characters
# # 4. Every second character
# print(text[0:3])
# print(text[3:7])
# print(text[-4:])
# print(text[1::2])

# #Q20, text = "I love Python"
# # Convert it to uppercase.
# # Convert it to lowercase.
# # Count how many times "Python" appears.
# # Replace "Python" with "Programming".
# text=input("Enter text: ")
# print(text.upper())
# print(text.lower())
# print(text.count("Python"))
# print(text.replace("python","java"))

# #Q21. List manipulation
# numbers = [10, 20, 30, 40, 50]
# # Add 60 to the end.
# # Add 5 at the beginning.
# # Remove 30.
# # Change 40 to 45.
# # Print the final list.
# numbers.append(60)
# numbers.insert(0,5)
# numbers.remove(30)
# numbers[3]=45
# print(numbers)

# #Q22. Take 5 numbers from the user, store them in a list, and then print:
# # The list
# # The largest number
# # The smallest number
# # The sum
# # The average
# # i=0
# numb=[]
# for i in range(5):
#     num=int(input())
#     numb.append(num)
# print(numb)

# lag=numb[0]
# small=numb[0]
# total=0
# avg=0
# for i in numb:
#     if i > lag:
#         lag=i
#     if i < small:
#         small=i
        
#     total+=i
# avg=total/len(numb)
# print(f"smallest is {small}")
# print(f"largest is {lag}")
# print(avg)
# print(total)
# #Q23. 
# a=[1,2,3,1,2,3,2,2,3]
# print(set())

# #Q24. Create a dictionary containing:
# name
# age
# college
# branch
# gpa

# Then:
# 1. Print the student's name.
# 2. Print the GPA.
# 3. Change the GPA.
# 4. Add a new key called year.
# 5. Print all key-value pairs using a loop.

# details= {
#     "name": "srujna",
#     "age": 21,
#     "college": "NMAMIT",
#     "branch": "CSE",
#     "gpa": 8.7
# }

# print(details["name"])
# print(details["gpa"])
# details["gpa"]=9.2
# details["year"]=2005
# for key, value in details:
#     print(key,value)

# # Q25. 
# students = [
#     {"name": "A", "marks": 85},
#     {"name": "B", "marks": 92},
#     {"name": "C", "marks": 76}
# ]
# for name, marks in students:
#     print(f"{name} scored {marks}")