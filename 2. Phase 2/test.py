# # 1. Student Result Calculator ⭐
# # Write a program that accepts a student's marks in 3 subjects.
# # Calculate and display:
# # - Total marks
# # - Average marks
# # - Whether the student passed or failed
# # A student passes only if they score at least 40 in every subject.
# total=0
# for i in range(3):
#     mark=int(input("Enter mark: "))
#     total+=mark
#     if mark < 40:
#         print("Failed")
#         break
# avg_mark=total/3
# print(total)
# print(avg_mark)

# # 2. Use these slabs:
# # Units	Rate
# # 0–100	₹2/unit
# # 101–200	₹3/unit
# # Above 200	₹5/unit
# # The program should ask for the number of units and calculate the total bill.
# units=int(input("Enter units: "))
# if units > 0 and units <= 100:
#     units*=2
# elif units <= 0:
#     print("Enter valid units")
# elif units >=101 and units <= 200:
#     units*=3
# else:
#     units*=5
# print(units)

# # 3. Take an integer as input and determine:
# # Whether it is positive, negative, or zero
# # Whether it is even or odd, if applicable
# num=int(input("Enter num: "))
# if num > 0:
#     if num % 2==0:
#         print("Positive and even num")
#     else:
#         print("Positive but odd num")
# elif num < 0:
#     if num % 2==0:
#         print("Negative and even num")
#     else:
#         print("Positive but odd num")
# else:
#     print("Zero")

# # 4. Countdown with Rules 
# # Take a positive integer n.
# # Print numbers from n down to 1.
# # However:
# # Skip numbers divisible by 3
# # Stop completely if you reach a number divisible by 7
# n=int(input("Enter positive n: "))
# if n > 0:
#     for i in range(n,1,-1):
#         if i%3==0:
#             continue
#         elif i%7==0:
#             break
#         else:
#             print(i)
# else:
#     print("Negative num")

# # 5. Class Performance Analyzer 
# # Ask the user how many students are in a class.
# # For each student, enter their marks.
# # Calculate:
# # Number of students who passed
# # Number who failed
# # Highest mark
# # Lowest mark
# # Average mark
# # Passing mark: 40.
# # Edge case: What should happen if the class contains 0 students?
# n=int(input("no of students: "))
# highest_mark=None
# lowest_mark=None
# total_mark=0
# count_passed=0
# count_failed=0
# if n > 0:
#     for i in range(1,n+1):
#         mark=int(input(f"enter mark of student{i}: "))
#         total_mark+=mark
#         if highest_mark is None or highest_mark < mark:
#             highest_mark=mark
#         if lowest_mark is None or lowest_mark > mark:
#             lowest_mark=mark
#         if mark >= 40:
#             count_passed+=1
#         else:
#             count_failed+=1
# else:
#     print("enter class that has strength greater than 0")
# if n > 0:
#     print("Avg mark: ", total_mark/n)
#     print(count_passed)
#     print(count_failed)
#     print(highest_mark)
#     print(lowest_mark)



    