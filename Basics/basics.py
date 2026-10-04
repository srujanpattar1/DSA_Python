# print("I'm an billionaire") #basic print statement

# #check the type of data type
# a=10
# print(type(a))

# #data types
# age=10
# name="srujan"
# salary=100000.98
# is_married=False
# gf=None
# print(type(age), type(name), type(salary), type(is_married), type(gf))

# f_name="srujan"
# l_name='pattar'
# print(f_name +" "+ l_name)
# print(10+69

# #taking input
# name=input("Enter name: ")
# print("hello", name)

# #type conversion
# age1=int(input("Enter age: "))
# age2=(input("Enter age: "))
# print(type(age1), type(age2))

# x="10"
# print(x+5) #error

# # Arithmetic operations
# a1=21
# b1=4
# print(a1+b1) #25
# print(a1-b1) #17
# print(a1*b1) #84
# print(a1/b1) #5.25
# print(a1//b1) #5
# print(a1%b1) #1
# print(a1**b1) #194481

# # for loop
# for i in range(5):
#     print("I'm a billionaire")

# for i in range(5):
#     print(i)

# for i in range(3, 7):
#     print(i)

# for i in range(0, 8, 2):
#    print(i) 

# for i in range(5, 0, -1):
#     print(i)

# for i in range(5):
#     if i == 2:
#         break
#     print(i)

# # In for (start, stop) => ending is not included in for
# # In for (start, stop, step)

# # while loop
# c=1
# while c<=5:
#     print(c)
#     c+=1

# (x=x+1) == (x+=1)
# (x=x-1) == (x-=1)

# #multiplication table
# num=int(input())
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")
    
# # outer and inner loop
# for i in range(1,3):
#     for j in range(1,3):
#         print(i,j)

# #String => sequence of characters, index will always start from 0 bcz, it is easy to calculate address and if it is at 0, move 0 positions from starting, move 1 position from starting
# name=" srujan pattar "
# print(name[0], name[-1]) #0th pos and -1 starts from the ending
# print(name[0:3]) #sru
# print(name[:3], name[3:]) #sru, jan
# print(name[::2]) #sua(exludes 2nd char)
# print(name[::-1]) #reverse
# print(name.upper()) #uppercase
# print(name.lower()) #lowercase
# print(name.strip()) #removes unnecessary space at the end and the start
# print(name.split()) #separates words into list
# print(name.replace("pattar", "m pattar"))

# marks=[46, 76, 29, 90]
# print(marks[3])
# marks[3]=5
# print(marks.append(3), marks) #adds ele at the end
# marks.insert(-1,100) #inserts at the particular pos
# print(marks)
# marks.remove(100) #removes the ele, should specify the value
# print(marks)
# marks.pop(1) #removes the last ele, if pos is specified it is also removed
# print(marks)
# print(len(marks))
# for mark in marks: #extracts all ele in list
#     print(mark)
# print(9 in marks) #checks if that ele exsists in list

# set1={1,2,3,2,3}
# print(set1.add(4))
# print(set1)
# print(set1.remove(4))
# print(set1)

# student = {
#   "name": "srujan",
#   "age": 21, 
#   "salary": 696969.69
# }
# print(student["name"])
# student["branch"]="cse"
# student["age"]=22
# print(student)

# for key,value in student.items(): print(key,value)

# def add(a,b):
#     return a+b
# print(add(4,5))
# print(add(10,-4))

# def greet(name): #parameter(place holder)
#     print("hello", name)
# greet("srujan") #argument(actual value)

# def sub1(a,b):
#     print(a-b)

# def sub2(a,b):
#     return(a-b)

# print(sub1(4,5))
# sub2(6,10)

# def calci(a,b):
#     return a+b, a-b
# x,y=calci(4,5)
# print(x)

# def is_even(a):
#     return a%2==0
# res=is_even(45)
# print(res)

# def greet(name="srujan"):
#     return "hello" + " " + name
# print(greet()) # No argument → use default
# print(greet("sristi")) #Argument given → use provided value

# def details(name, age, gender):
#     return(name,age,gender)
# print(details("srujan",34,"male")) #order doesn't matters

# def details1(name, age, gender):
#     return(name,age,gender)
# print(details1(name="srujan", gender="male", age=69)) #irrespective of order in the fun call we get the output

x=10 #global
def num():
    print(x)
num()

def num1():
    x1=10 #local, value of x is usable only inside this fun
    print(x1)
num1()
