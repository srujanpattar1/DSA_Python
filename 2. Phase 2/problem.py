# num=int(input("Enter number: "))
# while num!= -1 :
#     print("You entered: ", num)
#     num=int(input("Enter number: "))

# total=0
# for i in range(1,11):
#     total+=i
# print(total)

# i = 1
# while i <= 5:
#     if i == 3:
#         continue
#     print(i)
#     i += 1

# for i in range(0,5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(1,6):
#     for j in range(i):
#         print(i, end="")
#     print()

# Pattern 1: Counting
# Suppose we want:
# 1
# 2
# 3
# 4
# 5
# for i in range(1,6):
#     print(i)

# # Pattern 2: Repetition
# # 1
# # 22
# # 333
# # 4444
# # 55555
# for i in range(1,6):
#     for j in range(i):
#         print(i, end="")
#     print()

# # searching
# target=int(input("Enter target: "))
# for i in range(1,101):
#     if target == i:
#         print("Found 37")
#         break
    
# target=int(input("Enter target: "))
# flag=False
# for i in range(1, 101):
#     if target%2 == 0:
#         flag=True
#         break
# if flag:
#     print(f"{target} was found as an even number")
# else:
#     print(f"{target} was not found as an even number")

# #Problem 1: Sum of Even Numbers, Find the sum of all even numbers from 1 to 10.
# sum=0
# for i in range(1,11):
#     if i % 2 == 0:
#         sum += i
# print(sum)

# # Problem 2: Count Even Numbers, How many even numbers are there from 1 to 10?
# count=0
# for i in range(1,11):
#     if i % 2 == 0:
#         count += 1
# print(count)

# #Write a program that asks the user for a number n and then, Counts how many numbers from 1 to n are divisible by 3.
# n=int(input("Enter the num: "))
# count = 0
# for i in range(1, n+1):
#     if i % 3 == 0 :
#         print(i)
#         count += 1
# print(count)

# # Takes n and counts how many numbers from 1 to n are both even and divisible by 3.
# num=int(input("Enter num: "))
# count=0
# for i in range(1,num+1):
#     if i%2==0 and i%3==0:
#         count+=1
# print(count)

# #Find the largest number from: 10, 25, 7, 42, 18
# largest=7
# for i in range(7,44):
#     if i > largest:
#         largest=i
# print(largest)

# #the numbers one at a time through variables:
# a=10
# b=25
# c=7
# d=42
# e=18
# largest=a
# if a > largest:
#     largest=a
# if b> largest:
#     largest=b
# if c > largest:
#     largest=c
# if d > largest:
#     largest=d

# #smallest among this list
# numbers = [14, 3, 27, 8, 19, 2, 31]
# smallest=numbers[0]
# for i in numbers:
#     if i < smallest:
#         smallest=i
# print(smallest)

# numbers = [15, 22, 9, 40, 13, 18, 7, 30]
# # Find all three:
# # 1. Sum of numbers divisible by 3
# # 2. Count of numbers divisible by 3
# # 3. Largest number divisible by 3
# largest=None
# count=0
# total=0
# for i in numbers:
#     if i%5==0:
#         count+=1
#         total+=i
#         if largest is None or i > largest:
#             largest=i
# print(count)
# print(total)
# print(largest)

# Write a program that takes n from the user and finds:
# - How many numbers from 1 to n are divisible by 4
# - The sum of those numbers
# n=int(input("Enter n: "))
# count=0
# total=0
# for i in range(1,n+1):
#     if i%4==0:
#         count+=1
#         total+=i
# print(count, total)

# numbers = [17, 24, 9, 36, 13, 42, 8, 30]
# # Find the largest number divisible by 3. Your program should work even if the first element isn't divisible by 3.
# largest=None
# for num in numbers:
#     if num%3==0:
#         if largest is None or num > largest:
#             largest=num
# print(largest)

#  # Write a program that takes n and prints all numbers from 1 to n that are: divisible by 3 AND divisible by 5, Also count how many such numbers exist.
# n=int(input("Enter n: "))
# count=0
# for i in range(1, n+1):
#     if i%3==0 and i%5==0:
#         print(i)
#         count+=i
# print(count)

# # Write a program that:
# # 1. Takes a target number from the user.
# # 2. Searches for it in
# # 3. Prints "Found" if it exists.
# # 4. Otherwise prints "Not found".
# # 5. Stops searching immediately after finding it.
# numbers = [12, 7, 25, 18, 30, 9, 42]
# target=int(input("Enter target: "))
# for num in numbers:
#     if target == num:
#         print("Found")
#         break
# else:
#     print("Not found")

# # Write a program that finds:
# # 1. Number of even numbers
# # 2. Sum of even numbers
# # 3. Largest even number
# # 4. Number of odd numbers
# # 5. Sum of odd numbers
# # 6. Largest odd number
# numbers = [12, 7, 18, 5, 30, 11, 24, 9, 40, 15]
# count_even=0
# sum_even=0
# largest_even=None
# count_odd=0
# sum_odd=0
# largest_odd=None
# for num in numbers:
#     if num%2==0:
#         count_even+=1
#         sum_even+=num
#         if largest_even is None or num > largest_even:
#             largest_even=num

#     if num%2!=0:
#         count_odd+=1
#         sum_odd+=num
#         if largest_odd is None or num > largest_odd:
#             largest_odd=num
# print(count_even)
# print(count_odd)
# print(sum_even)
# print(sum_odd)
# print(largest_even)
# print(largest_odd)

# Project Goal
# Build a program that analyzes a student's marks.
# The program should ask for:
# - Student name
# - Number of subjects
# - Marks for each subject
# Then calculate:
# 1. Total marks
# 2. Average marks
# 3. Highest mark
# 4. Lowest mark
# 5. Number of subjects passed
# 6. Number of subjects failed
# 7. Whether the student passed overall
name=input("Enter name: ")
num_of_sub=int(input("Number of subjects: "))
total_mark=0
avg_mark=0
highest_mark=None
lowest_mark=None
count_passed=0
count_failed=0
flag=False
for i in range(1, num_of_sub+1):
    mark=int(input(f"Enter subject {i} marks: "))
    if mark <= 0:
        print("Enter valid marks ")
        break
    else:
        total_mark+=mark
        if highest_mark is None or mark > highest_mark:
            highest_mark=mark
        if lowest_mark is None or mark < lowest_mark:
            lowest_mark=mark
        if mark >= 40:
            count_passed+=1
        else:
            count_failed+=1
        if mark < 40:
            flag=True

print("Total mark: ", total_mark)
avg_mark=total_mark/num_of_sub
print("Avg mark: ", avg_mark)
print("Highest mark: ", highest_mark)
print("Lowest mark: ", lowest_mark)
print("No of subjects passed: ", count_passed)
print("No of subjects failed: ",count_failed)
if flag:
    print("Failed overall")
        
    
