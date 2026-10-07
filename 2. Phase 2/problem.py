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
    
target=int(input("Enter target: "))
flag=False
for i in range(1, 101):
    if target%2 == 0:
        flag=True
        break
if flag:
    print(f"{target} was found as an even number")
else:
    print(f"{target} was not found as an even number")
    