# Phase 3: Python Data Structures 🚀
- List
- Tuples
- Set
- Dictionaries

## List
- []
- collection of elemenets of different data structure
- mutable 
- ordered

### List 
ex- numb=[10,20,30,40,50]
- len() tells you how many elements exist -> print(len(numb))
- Travsing => Traversal means visiting the elements one by one. -> for num in number: print(num)

### List methods:
- append() adds an element to the end -> print(numb.append(60))
- insert() adds an element at a specific index -> print(numb.insert(1,90))
- remove() removes the first matching occurence value, not all the values -> print(numb.remove(20))
- pop() uses a position to remove the element, if no pos is specified then last element is removed, only pop returns the value -> print(numb.pop(2))
- sort() -> modifies the list and returns none, sorted() -> creates a new list of sorted order and returns it, 
ex: x=numb.sort(numb) => returns none, modifies the original list and sorts it
    y=sorted(numb) => return new list of sorted order
- reverse() -> reverses the original list and returns None. numb[::-1] -> reverses the original list and returns list -> print(numb.reverse())

Note:
a=[1,2,3]
b=a
c=a.copy()
b.append(3)
print(a)
print(b)
print(c)
print(b is a)
- is checks whether two variables refer to the same object, not whether their contents are equal. 
- copy is used to take a copy of a list and store it independently

Note:
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b) #checks are the values same
print(a is b) #both are pointing to different list with same value

### list[start:stop:step] #slicing
- Positive step: move left to right.
- Negative step: move right to left.
- The start index is included.
- The stop index is excluded.
- The step determines how many positions to move between selected elements.
- in checks whether a value exists in the list. not in checks whether a value does not exist. Both returns answers in boolean

Ex- 
a=[10,20,30,40]
print(a[::])

### Ways of adding into list-
num=[1,2,3,4,5]
- num.append([1,2,3]) #adds entire new list as a single value into original list
- num.extend([4,5,6]) #adds all the elements from the given list into original list
- num.insert(6,6) #adds value at the mentioned index

### Ways of deleting into list-
num1=[1,2,3,4,2]
- a=num1.pop(1) #removes the value in index 1 and does return the value
- del num1[1] #remoces the value in index 1 and doesn't return the value
- num1.remove(2) #removes the first apperaing 2

Note: 
a=[1,2]
b=a
a+=[3] //modifies the given list
a=a+[4] //creates a new list and reassigns it
a.append(5)
print(a)
print(b)

## Tuples
- ()
- ordered collection of elements
- indexed
- not mutable 

Note: 
a=(1) #int
a=(1,) #tuple

### tuple unpacking
details=("srujan", 21, "CSE")
name, age, branch=details
print(name)
print(details[0])


## Sets
- {}
- collection of unique elements, removes duplicate values
Note: 
a = {}
b = set()
print(type(a)) #dict
print(type(b)) #set

### Set Manipulation
#### Removing
a={1,2,3,4,1,2,4}
a.discard(6) #if that value doesn't exists, it will not throw an error
a.remove(6) #if that value doesn't exists, it will throw key error

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A|B) #All unique elements from both sets.
print(A&B) #Elements common in both the sets.
print(A^B) #Elements that are not common.
print(A-B) #elemetns in A that aren't in B.
print(B-A) #elemetns in B that aren't in A.

Note:
num=[2,3,4,5,2,3,4,9,7]
converted=set(num) #to convert into set, in random order
convert=list(dict.fromkeys(num)) #to convert into set, in same order of list
print(convert)

## Dictionary 
- {}
- mutuable
- stores data in key value pair
- keys -> should be unique, if repeated last assigned value will be considered
- values -> multiple keys can have same values

details={
    "name":"srujan",
    "age":21,
    "branch":"cse",
    "name":"sristi"
}

### Accessing the key:
print(details["cgpa"]) #raises error if that key is not found
print(details.get("cgpa", "hello")) #if not found, doesn't raises any error, if key value is not found, then default value will display

### Adding, Updating and Removing
details["name"]="Srujan" #updating the new value to the existsing key
details["cgpa"]=9.1 #added new key value pair
del details["age"] #deleting the key
print(details)  
print("Gender" in details) #checking is that key present in the dict

Note: 
print(details.keys()) #returns all the keys only
print(details.values()) #returns all the values only
print(details.items()) #returns key value pair in tuples

uisng for loop and .items(), to iterate:
shop={
    "apple":50,
    "mango":90,
    "green_apple":30
}
for fruit, price in shop.items():
    if price > 40:
        print(fruit,price)


### Different ways of deleting key value pair
del shop["apple"] #removes that key
x=shop.pop("mango") #removes that key and stores in var x
shop.clear() #deletes entire dict

### Frequency in dict
frequency={}
numbers=[2,3,4,2,3,5,8]
for num in numbers:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
print(frequency)

for num in numbers:
    frequency[num]=frequency.get(num,0)+1 
print(frequency)

## Nested Data structure
- one data structure within another data structure
- 