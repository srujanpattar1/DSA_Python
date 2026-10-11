# # 1. Student Result Calculator 
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

# # 6. ATM Withdrawal Validator 
# # Create a simple ATM withdrawal program.
# # Ask for:
# # - Account balance
# # - Withdrawal amount
# # The withdrawal is allowed only if:
# # 1. Withdrawal amount is positive.
# # 2. Withdrawal amount does not exceed the balance.
# # 3. Withdrawal amount is a multiple of 100.
# # Display an appropriate message for each situation.
# balance=int(input("balance: "))
# withdraw=int(input("withdraw: "))
# if withdraw > 0 and withdraw %10 == 0 and withdraw < balance :
#     balance-=withdraw
#     print("balance: ", balance)
# else:
#     print("Enter positive balance")
# if balance %10 != 0:
#     print("Enter withdrawal in multiples of 100 only")
# if withdraw > balance:
#     print("enter withdrwal less than balance")

# # 7. Number Statistics
# # Ask the user to enter positive integers repeatedly.
# # The input ends when the user enters -1.
# # Before stopping, calculate:
# # - Number of values entered
# # - Sum
# # - Average
# # - Largest value
# # - Smallest value
# # - Number of even values
# # - Number of odd values
# # Do not include -1 in the calculations.
# num=int(input("Enter positive num: "))
# sum_num=0
# count_num=0
# avg_num=0
# largest_num=None
# smallest_num=None
# no_of_even=0
# no_of_odd=0
# if num > 0:
#     while num > 0:
#         sum_num+=num
#         count_num+=1
#         if num%2==0:
#             no_of_even+=1
#         else:
#             no_of_odd+=1
#         if largest_num is None or largest_num > num:
#             largest_num=num
#         if smallest_num is None or smallest_num < num:
#             smallest_num=num
#         num=int(input("Enter positive num: "))
# else:
#  print("Enter positive num")   
# print("Sum: ", sum_num)
# print("total count: ", count_num)
# print("Avg: ", sum_num/count_num)
# print("Largest: ", largest_num)
# print("Smallest: ", smallest_num)
# print("Even count: ", no_of_even)
# print("Odd count: ", no_of_odd)

# # 8. Password Validator 
# # Ask the user to enter a password.
# # The password is considered valid only if:
# # - It contains at least 8 characters
# # - Its first character is not a space
# # - It contains at least one digit
# # - It contains at least one uppercase letter
# # You may use only the string operations you've learned so far.
# # Display whether the password is valid or invalid.
# password=input("Enter the password: ")
# if len(password) >= 8:
#     if password[0] != " ":
#         print("Valid password")
# else:
#     print("Invalid password")

#  # 9. Prime Number Analyzer 
#  # Take a positive integer n.
#  # Determine whether n is prime.
#  # Then, if it is not prime, display whether it is:
#  # - Even
#  # - Odd
#  # Also display the number of divisors it has.
# num=int(input("Enter num: "))
# count=0
# if num > 0:
#     for i in range(2,num):
#         if num%i==0:
#             count+=1
#             print("It is not a prime number")
#             if num%2==0:
#                 print("it is even")
#             else:
#                 print("it is odd")
#             break
#     else:
#         print("It is a prime num")
# print("count=",count+2)           

# 10. Digital Sum and Reverse 
# Take a positive integer and perform two operations:
# 1. Find the sum of its digits.
# 2. Reverse the number.
num=input("Enter num: ")
sum=0
for i in num[::-1]:
    print(i, end="")
    sum+=int(i)
print("Sum: ", sum)