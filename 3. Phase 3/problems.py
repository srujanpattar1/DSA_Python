# numb=[10,20,30,40,50]
# print(len(numb))
# for num in numb:
#     print(num)
# for i in range(len(numb)):
#     print(numb[i])

# for i in range(len(numb)):
#     if numb[i]%4==0:
#         numb[i]=numb[i]+10
# print(numb)

# x=numb.sort()
# y=sorted(numb)
# print(x,y)

# result=numb
# result.append(30)
# print(result)
# print(numb)

# a=[1,2,3]
# b=a
# c=a.copy()
# b.append(3)
# print(a)
# print(b)
# print(c)
# print(b is a)

# a=[1,2,3,4]
# b=[1,2,3,4]
# print(a==b) #checks are the values same
# print(a is b) #both are pointing to different list with same value

# numbers = [5, 10, 15, 20, 25, 30]
# print(numbers[1:5:2])
# print(numbers[-4:-1])
# print(numbers[::-1])

# a=[10,20,30,40,50,20]
# print(a[::]) #[10,20,30,40,50,20]
# print(a[1:4:2]) #[20,40]
# print(a[-1:-5:-1]) #[30,40,50,20]
# print(a[::-1]) #[20, 50,40,30,20,10]
# print(a[::2]) #[10,30,50]
# print(60 not in a)
# print(a.index(20))
# print(a.count(20))
# print(a.index(100)) #error bcz it doesn't exists
# print(a.count(100))

# Write a Python program that:
# # 1. Takes a list of integers: [12, 7, 12, 5, 7, 12]
# # 2. Prints how many times 12 occurs.
# # 3. Prints the index of the first occurrence of 7.
# # 4. Checks whether 10 exists in the list.
# # 5. Prints "Found" if 10 exists, otherwise "Not found".
# hello=[12, 7, 12, 5, 7, 12]
# print(hello.count(12)) #3
# print(hello.index(7)) #1
# print(10 in hello) #False
# if 10 in hello: #Not found
#     print("Found")
# else:
#     print("Not Found")

# numbers = [5, 10, 15, 10, 20]
# # target=10
# # if target in numbers:
# #     print("Index:", numbers.index(10))
# # else:
# #     print("Not found")
# largest=0
# for num in numbers:
#     if num > largest:
#         largest=num
# print(largest)

# numbers = [12, 7, 25, 9, 31, 18]
# largest = 0
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)

# numbers = [12, -4, 25, -9, 3, 18]
# # # Calculate and print:
# # # 1. The sum of all numbers.
# # # 2. How many numbers are positive.
# # # 3. The largest number.
# # # 4. The smallest number.
# if not numbers:
#     print("It is empty")
# else: 
#     total=0
#     largest=numbers[0]
#     smallest=numbers[0]
#     count=0
#     for num in numbers:
#         total+=num
#         if num > 0:
#             count += 1
#         if num > largest:
#             largest=num
#         if num<smallest:
#             smallest=num
#         print(largest)
#         print(smallest)
#         print(count)
#         print(total)
        
# list1=[1]
# if not list1 :
#     print("it is empty")
# else:
#     print("It is not empty")

# num=[1,2,3,4,5]
# num.append([1,2,3]) #adds entire new list as a single value
# print(num)
# num.extend([4,5,6]) #adds all the elements from the given list into original list
# print(num)
# num.insert(6,6) #adds value at the mentioned index
# print(num)
# print(num[5])

# num1=[1,2,3,4,2]
# # a=num1.pop(1) #removes the value in index 1 and does return the value
# # del num1[1] #remoces the value in index 1 and doesn't return the value
# # num1.remove(2) #removes the first apperaing 2
# num1.clear()
# print(num1)

# a=[1,2]
# b=a
# a+=[3]
# a=a+[4]
# a.append(5)
# print(a)
# print(b)

# details=("srujan", 21, "CSE")
# name, age, branch=details
# print(name)
# print(details[0])

# a=5
# b=10
# c=15
# a,b,c=c,a,b

# valuee="srujan",30,"asd",20,304,50
# a,*b,c=valuee
# print(a)
# print(b)
# print(c)
# print(type(b))

# values=(1,2,3,4)
# a,*b=values
# b.append(8)
# print(a)
# print(b)
# print(values)

# value={1,2,3,4,1,2,3,4}
# value.add(4)
# value.add(5)
# print(value)

# a={1,2,3,4,1,2,4}
# a.discard(6) #if that value doesn't exists, it will not throw an error
# a.remove(6) #if that value doesn't exists, it will throw key error

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A|B) #All unique elements from both sets.
# print(A&B) #Elements common in both the sets.
# print(A-B) #elemetns in A that aren't in B.
# print(A^B) #Elements that are not common.

# num=[2,3,4,5,2,3,4,9,7]
# converted=set(num) #to convert into set, in random order
# convert=list(dict.fromkeys(num)) #to convert into set, in same order of list
# print(convert)

details={
    "name":"srujan",
    "age":21,
    "branch":"cse",
    "name":"sristi"
}
print(details["name"]) #latest name key's value will print, "sristi"

### accessing values
print(details["cgpa"]) #raises error if that key is not found
print(details.get("cgpa", "hello")) #if not found, doesn't raises any error, if key value is not found, then default value will display

